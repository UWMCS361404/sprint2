from user import User
from user import User
from google.appengine.ext import ndb

class Question(ndb.Model):
    owner = User
    topic = ndb.StringProperty()
    answered = ndb.BooleanProperty();
    messages = []
    className = "CS361" # Hard coded for now
    
    def setOwner(self, owner):
        self.owner = owner
        
    def getOwner(self):
        return self.owner        

    def setTopic(self, topic):
        self.topic = topic
    
    def getTopic(self):
        return self.topic
        
    def close():
        self.answered = True
    
    def getAnswered(self):
        return self.answered
    
    def getSizeOfThread(self):
        return len(messages)
        
    def setMessages(self, messages):
        self.messages = messages
        
    def getMessages(self):
        return self.messages
    
    