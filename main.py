import webapp2
import jinja2
import os
import datetime

from google.appengine.ext import ndb
from user import *
from util import *
from message import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)

class Login(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('login.html')
        
        template_values = {
            'Test': 'tst'
        }

        self.response.write(template.render(template_values))
        
    def post(self):
        uNm = self.request.get('uName')
        uPwd = self.request.get('uPass')
        
        validAcc = False
        
        for item in userList:
            if item.getName() == uNm.strip() and item.getPwd().strip() == uPwd:
                validAcc = True
                
        if validAcc == False:
            self.redirect("/")
        
        if validAcc == True:
            self.response.set_cookie("CurrentUser", uNm, max_age=360, path="/")
            self.redirect("/messcenter?user="+uNm)

class MessCenter(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('messcenter.html')
        
        uNm = self.request.get("user")

        template_values = {
            "user": uNm,
            "userList": userList,
        }
        
        self.response.write(template.render(template_values))
    
    def post(self):
        student = self.request.get("studentName")
        self.redirect("/chat?student=" + student)

class Chat(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('chat.html')
        
        student = self.request.get("student")
        user = self.request.cookies.get("CurrentUser")
        
        if student == "":
            student = getInstrAccount(userList).getName()
            
        #print("\n\t\t This is the student: " + repr(str(student)))
        self.response.set_cookie("receiver", student, max_age=360, path="/")
        # {% if message.getSender().getName() == user or message.getReceiver().getName() == student %}
        messages = list(Message.query())
        print("\n\t\t" + student)
        template_values = {
            "user": user,
            "student": student,
            "messages": messages,
            "size": len(messages)  
        }

        self.response.write(template.render(template_values))
        
    def post(self):
        user = self.request.cookies.get("CurrentUser")

        message = Message(time=datetime.datetime.now(), content=self.request.get("message"), sender=getAccount(user, userList), receiver=getAccount(self.request.cookies.get("receiver"), userList))
        
        print(getAccount(self.request.cookies.get("receiver"), userList))
        print(message.getReceiver())
        message.put()
        
        self.redirect("/messcenter?user=" + user)

userList = parseTxt("accounts.csv")

app = webapp2.WSGIApplication([
	('/', Login),
	('/messcenter', MessCenter),
	('/chat', Chat)
], debug=True)

