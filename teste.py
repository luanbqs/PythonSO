from time import sleep
from random import randint

class Row:
    def __init__ (self, timeSlice):
        self.timeSlice = timeSlice

    def getTimeSlice(self):
        return self.timeSlice

class Process:
    def __init__ (self, tempoExec):
        self.tempoExec = tempoExec
        self.qtdIOs = 0
        self.tempoIOs=[]

    def adicionarIOs(self):
        self.qtdIOs = randint(0,9)
        for i in range (self.qtdIOs):
            self.tempoIOs.append(randint(0,30))  
        print('---------->',self.tempoIOs)

    

class Cpu:
    def __init__(self,array):
        self.array=array
        

row1=Row(2)
row2=Row(5)
row3=Row(10)
row4=Row(15)

p1=Process(20)
p1.adicionarIOs()
p2=Process(10)
p2.adicionarIOs()
p3=Process(50)
p3.adicionarIOs()

array=[]
array.append(p1)
array.append(p2)
array.append(p2)



        

    

