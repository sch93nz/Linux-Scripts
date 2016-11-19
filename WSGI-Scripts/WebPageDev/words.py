


class Heading(object):
    text = ""
    webChildren = list()


    def __init__(self,words):
        self.text = words

    def getOpening(self):
        output = '''\r\n<h1'''
        output += ''' style="'''
        return output+'''">'''

    def getEnding(self):
        return '''</h1>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        
        for item in self.webChildren:
            output+=item.getbody

        output+=self.getEnding()

        return output

