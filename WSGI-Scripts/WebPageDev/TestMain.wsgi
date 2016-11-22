from Page import *
from words import *
from Layout import *

def startTest():
    a = Page("lizard")

    c = div()
    c.add(H1("hello"))
    c.add(br())

    a.add2Head(c)
    b = div()
    a.add2Body(b)
    b.add(br())
    b.add(H2("this fixed"))
    b.add(br())
    b.add(P("so this a test paragraph for as to read to make sure its all going correctly."))
    

    print(a.webString())
    f = open('Test.html','w')
    f.write(a.webString())

if __name__ == "__main__":
    startTest()