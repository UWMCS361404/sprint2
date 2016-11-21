import webapp2
import jinja2
import os
import time
import datetime
import calendar

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
            
        self.response.set_cookie("receiver", student, max_age=360, path="/")
        messages = list(Message.query().order(Message.time, -Message.time))

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
        
        message.put()
        
        self.redirect("/messcenter?user=" + user)
        
class Faq(webapp2.RequestHandler):
    def get(self): 
        template = JINJA_ENVIRONMENT.get_template('faq.html')
        user = self.request.cookies.get("CurrentUser")
        
        template_values = {
            "user": user            
        }
        
        self.response.write(template.render(template_values))
        
    def post(self):
        user = self.request.cookies.get("CurrentUser")
        self.redirect("/messcenter?user=" + user)
        

userList = parseTxt("accounts.csv")

app = webapp2.WSGIApplication([
	('/', Login),
	('/messcenter', MessCenter),
	('/chat', Chat),
	('/faq', Faq)
], debug=True)
