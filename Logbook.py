import datetime
import sys

class Week:
    shifts=[]

    def __init__(self):
        self.shifts = []

    def add(self, s):
        self.shifts.append(s)

    def writeOut(self):
        temp =""
        for A in self.shifts:
            temp+=A.writeout()


class shift:

    start = datetime.datetime.now()
    end = datetime.datetime.now()

   
    def __init__(self,s,e):
        self.start = datetime.datetime.strptime(s,"%a %d-%m-%Y %b  %I:%M:%S %p")
        if e != '':
            self.end = datetime.datetime.strptime(e,"%a %d-%m-%Y %b  %I:%M:%S %p")
        else:
            self.end = ''

    def end(self, e):
        self.end = end

    def isComplete(self):
        if self.end == '':
            return False
        else:
            return True
    
    def timeWorked(self):
        if  self.isComplete():
            dif = self.start - self.end
            return dif.strftime("%H:%M")
        else:
            return "error"  

    def writeout(self):
        if self.isComplete():
            return self.start.strftime("%a %d-%m-%Y %b  %I:%M:%S %p")+"\t"+self.end.strftime("%a %d-%m-%Y %b  %I:%M:%S %p")+"\n"
        else:
            return ""+self.start.strftime("%a %d-%m-%Y %b  %I:%M:%S %p")+"\t"

week = Week
current = shift

def LoadWeek():
    Date = datetime.datetime.now()
    name = "Work_log_"+Date.strftime("%W")+".logbook"
    file = open(name,'r')
    week = Week()
    if Date.weekday() == 0:
        return
    else:
        
        content = file.readlines()
        for line in content:
            start,end = line.split("\t")
            temp
            if end != '':
                temp = shift(start,end)
            else:
                temp = shift(start,'')
                current = temp 

            week.add(temp)


def stampOn():
    Date = datetime.datetime.now()
    current = shift(Date.strftime("%a %d-%m-%Y %b  %I:%M:%S %p"),'')
    week.add(week,current)
    print(week.writeOut(week))

    
def stampOff():
    Date = datetime.datetime.now()
    current.add(Date)
  


if __name__ == "__main__":
    LoadWeek()
    for arg in sys.argv:
        arg = str(arg)
        if arg == "stampON":
            stampOn()
            print("stampON")
        elif arg == "stampOFF":
            stampOff()
        elif arg != "Logbook.py":
            print ("error use ether stampON or stampOFF")


        


