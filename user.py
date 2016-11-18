class User:
    def __init__(self, name="", pwd="", aType=""):
        self.name = name
        self.pwd = pwd
        self.aType = aType
        #self.classList = []
        #self.className = StringProperty()

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
        
    def setPwd(self, pwd):
        self.pwd = pwd
        
    def getPwd(self):
        return self.pwd
        
    def setaType(self, aType):
        self.aType = aType
    
    def getaType(self):
        return self.aType
        
    def setclassList(self, list):
        self.classList = list
        
    def getclassList(self):
        return self.classList
        
    def toString(self):
        return str(name) + "," + str(pwd) + "," + str(aType)
