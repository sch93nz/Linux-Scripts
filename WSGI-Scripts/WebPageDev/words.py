import random

class A(object):

    ID = 0
    link = ""
    webChildren = list()


    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
        self.link = words

    def getOpening(self):
        output = '''\r\n<a'''
        return output+'''">'''

    def getEnding(self):
        return '''</a>'''

    def webString(self):

        output = self.getOpening()
        output += self.link
        
        for item in self.webChildren:
            output+=item.webString()

        output+=self.getEnding()

        return output

class P(object):
    ID = 0
    text = ""
    webChildren = list()
    

    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
        self.text = words

    def getOpening(self):
        output = '''\r\n<p'''
        output += ''' style="'''
        return output+'''">'''

    def getEnding(self):
        return '''</p>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        
        for item in self.webChildren:
            output+=item.webString()

        output+=self.getEnding()

        return output

class H1(object):
    ID = 0
    text = ""
    webChildren = list()
    

    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
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
            output+=item.webString()

        output+=self.getEnding()

        return output


class H2(object):
    ID=0
    text = ""
    webChildren = list()
    

    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
        self.text = words

    def getOpening(self):
        output = '''\r\n<h2'''
        output += ''' style="'''
        return output+'''">'''

    def getEnding(self):
        return '''</h2>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        
        for item in self.webChildren:
            output+=item.webString()

        output+=self.getEnding()

        return output

class H3(object):
    ID=0
    text = ""
    webChildren = list()
    

    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
        self.text = words

    def getOpening(self):
        output = '''\r\n<h3'''
        output += ''' style="'''
        return output+'''">'''

    def getEnding(self):
        return '''</h3>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        
        for item in self.webChildren:
            output+=item.webString()

        output+=self.getEnding()

        return output

class H4(object):
    text = ""
    webChildren = list()
    ID=0

    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
        self.text = words

    def getOpening(self):
        output = '''\r\n<h4'''
        output += ''' style="'''
        return output+'''">'''

    def getEnding(self):
        return '''</h4>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        
        for item in self.webChildren:
            output+=item.webString()

        output+=self.getEnding()

        return output

class H5(object):
    text = ""
    webChildren = list()
    ID=0

    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
        self.text = words

    def getOpening(self):
        output = '''\r\n<h5'''
        output += ''' style="'''
        return output+'''">'''

    def getEnding(self):
        return '''</h5>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        
        for item in self.webChildren:
            output+=item.webString()

        output+=self.getEnding()

        return output

class H6(object):
    text = ""
    webChildren = list()
    ID=0

    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
        self.text = words

    def getOpening(self):
        output = '''\r\n<h6'''
        output += ''' style="'''
        return output+'''">'''

    def getEnding(self):
        return '''</h6>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        
        for item in self.webChildren:
            output+=item.webString()

        output+=self.getEnding()

        return output

class H7(object):
    text = ""
    webChildren = list()
    ID=0

    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
        self.text = words

    def getOpening(self):
        output = '''\r\n<h7'''
        output += ''' style="'''
        return output+'''">'''

    def getEnding(self):
        return '''</h7>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        
        for item in self.webChildren:
            output+=item.webString()

        output+=self.getEnding()

        return output

class H8(object):
    text = ""
    webChildren = list()
    ID=0

    def __init__(self,words):
        self.webChildren=[]
        self.ID =random.getrandbits(16)
        self.text = words

    def getOpening(self):
        output = '''\r\n<h8'''
        output += ''' style="'''
        return output+'''">'''

    def getEnding(self):
        return '''</h8>'''

    def webString(self):

        output = self.getOpening()
        output += self.text
        
        for item in self.webChildren:
            output+=item.webString()

        output+=self.getEnding()

        return output


