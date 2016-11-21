import datetime
from user import *
from util import *
from google.appengine.ext import ndb

class Message(ndb.Model):
    time = ndb.DateTimeProperty()
    content = ndb.StringProperty()
    sender = ndb.StructuredProperty(User)
    receiver = ndb.StructuredProperty(User)

    def setSender(self, sender):
        self.sender = sender

    def getSender(self):
        return self.getSender()

    def setReceiver(self, receiver):
        self.receiver = receiver
        
    def getReceiver(self, receiver):
        return self.getreceiver

    def getSender(self):
        return self.sender

    def messagesWith(self, user):
        query = Message.query()

    def messagesFrom(self, user):
        query = Message.query()
        return (list(query.filter(Message.sender == user)))

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
Contact GitHub API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Status Help
