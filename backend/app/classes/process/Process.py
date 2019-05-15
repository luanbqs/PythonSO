from time import sleep
from random import randint

class Process:
    def __init__ (self, tempoExec):
        self.tempoExec = tempoExec
        self.qtdIOs = 0
        self.tempoIOs=[]

    def adicionarIOs(self):
        self.qtdIOs = randint(0,9)
        for i in range (self.qtdIOs):
            self.tempoIOs.append(randint(0,30)) 