import datetime
from user import User
from google.appengine.ext import ndb

class Message(ndb.Model):

    time = ndb.DateTimeProperty()
    content = ndb.StringProperty()
    
    def setSender(self, sender):
        self.sender = sender
        
    def getSender(self):
        return self.sender
        
    def setReceiver(self, receiver):
        self.receiver = receiver
        
    def getReceiver(self):
        return self.receiver
        
    def setTime(self, time):
        self.time = time
        
    def getTime(self):
        return self.time
        
    def setContent(self, content):
        self.content = content
        
    def getContent(self):
        return self.content
