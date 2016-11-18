import webapp2
import jinja2
import os
import datetime

from google.appengine.ext import ndb
from user import User
from util import *
from message import Message

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
            if item.getName() == uNm and item.getPwd() == uPwd:
                validAcc = True
        
        if validAcc == False:
            self.redirect("/")
        
        if validAcc == True:
        
            self.response.set_cookie("loginName", uNm, max_age=360, path="/")
            self.redirect("/messcenter?user="+uNm)

class MessCenter(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('messcenter.html')
        
        messages = list(Message.query())
        uNm = self.request.get("user")
        template_values = {
            "user": uNm,
            "userList": userList,
        }
        
        self.response.write(template.render(template_values))
    
    def post(self):
        student = self.request.get("studentName")
        self.redirect("/chat?student=" + student);

class Chat(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('chat.html')
        
        student = self.request.get("student")
        user = self.request.cookies.get("loginName")
        messages = list(Message.query())
        
        template_values = {
            "user": user,
            "student": student,
            "messages": messages
        }
        
        self.response.write(template.render(template_values))
        
    def post(self):    
        user = self.request.cookies.get("loginName")
        
        message = Message(time=datetime.datetime.now(), content=self.request.get("message"));
        message.setSender(getAccount(user))
        message.setReceiver(self.request.get("student"));
        
        message.put()
        
        self.redirect("/messcenter?user=" + user)
        #self.redirect("/messcenter?user=" + user + "&" + "message=" + self.request.get("message"));

app = webapp2.WSGIApplication([
	('/', Login),
	('/messcenter', MessCenter),
	('/chat', Chat)
], debug=True)

userList = parseTxt("accounts.csv")
