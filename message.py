import datetime
from google.appengine.ext import ndb

class Message(ndb.Model):

    rName = ndb.StringProperty()
    sName = ndb.StringProperty()
    time = ndb.DateTimeProperty()
    content = ndb.StringProperty()
    
    def setrName(self, rName):
        self.rName = rName
    
    def getrName(self):
        return self.rName
        
    def setsName(self, sName):
        self.sName = sName
        
    def getsName(self):
        return self.sName
        
    def setTime(self, time):
        self.time = time
        
    def getTime(self):
        return self.time
        
    def setContent(self, content):
        self.content = content
        
    def getContent(self):
        return self.content
