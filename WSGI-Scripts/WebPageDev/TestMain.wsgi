from Page import *
from words import *

def startTest():
    a = Page("lizard")
   
    b = Heading("hello")
    a.add2Head(b)
    f = open('Test.html','w')
    f.write(a.webString())

if __name__ == "__main__":
    startTest()