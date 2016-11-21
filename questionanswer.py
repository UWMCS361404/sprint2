from google.appengine.ext import ndb

class questionAnswer(ndb.Model):
    
    heading = ndb.StringProperty()
    question = ndb.StringProperty()
    answer = ndb.StringProperty()
    
    def getHeading(self):
        return self.heading
        
    def getQuestion(self):
        return self.question
        
    def getAnswer(self):
        return self.answer