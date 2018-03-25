class check:
    def __init__(self,):
        self.dic={}
        
    def addJsonStruct(self,file):
        f=open(file,"r")
        for linea in f:
            self.dic[linea.rstrip('\n')]=""



    