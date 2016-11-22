import random


class br(object):

    def webString(self):
        return "<br>"

class colgroup(object):

    webChildren = list()
    ID = 0

    def __init__(self):
         self.webChildren=[]
         self.ID =random.getrandbits(16)

    def add(self, item):
        self.webChildren.append(item)

    def getOpening(self):
        return '''\r\n<colgroup>'''

    def getEnding(self):
        return '''</colgroup>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        for item in self.webChildren:
            output+=item.webString()
        output+=self.getEnding()

        return output

class col(object):

    ID = 0

    def __init__(self, id):
        self.ID = id

    def webString(self):
         return "<col>"

class div(object):

    webChildren = list()
    ID = 0

    def __init__(self):
         self.webChildren=[]
         self.ID =random.getrandbits(16)
        

    def add(self, item):
        self.webChildren.append(item)

    def getOpening(self):
         return''' \r\n<div>'''

    def getEnding(self):
        return '''</div>'''

    def webString(self):

        output = self.getOpening()

        for item in self.webChildren:
            #print(item)
            output+=item.webString()

        output+=self.getEnding()

        return output