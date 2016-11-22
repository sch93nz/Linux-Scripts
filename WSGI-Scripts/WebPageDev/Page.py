

class Title(object):
    text = ""
  
    def __init__(self,words):
        self.text = words


    def getOpening(self):
        return '''\r\n<title>'''

    def getEnding(self):
        return '''</title>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        output+=self.getEnding()

        return output

class Head(object):
        webChildren = list()

        def add(self,item):
            self.webChildren.append(item)

        def getOpening(self):
            return '''\r\n<head>'''

        def getEnding(self):
            return '''\r\n</head>''' 

        def webString(self):

            output = self.getOpening(self)

            for item in self.webChildren:
              
                output+=item.webString()

            output+=self.getEnding(self)

            return output


class Body(object):
        webChildren = list()

        def add(self,item):
            self.webChildren.append(item)

        def getOpening(self):
            return '''\r\n<body>'''

        def getEnding(self):
            return '''\r\n</body>'''

        def webString(self):

            output = self.getOpening(self)

            for item in self.webChildren:
                output+=item.webString()

            output+=self.getEnding(self)

            return output

class Page(object):

        head = Head
        body = Body

        def __init__(self,title):
            self.head.add(self.head,Title(title))

        def add2Head(self, item):
            self.head.add(self.head,item)

        def add2Body(self,item):
            self.body.add(self.body,item)

        def getOpening(self):
            return '''<!DOCTYPE html>\r\n<html>'''

        def getEnding(self):
            return '''\r\n</html>'''

        def webString(self):

            output = self.getOpening()

            output+= self.head.webString(self.head)

            output+= self.body.webString(self.body)

            output+=self.getEnding()

            return output


