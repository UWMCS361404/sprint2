import webapp2
import jinja2
import os

from user import User
from util import parseTxt

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)

userList = []

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
                #print(repr(item.getaType())) # Note that the function, repr shows white space characters. I'm not sure where the \r\n is coming from, but this works for now
                #print(item.getaType() == "'ui")
                #if item.getaType() == "i\r\n":
                #    print("Instr")
                validAcc = True
        
        if validAcc == False:
            self.redirect("/")
        
        if validAcc == True:
        
            self.response.set_cookie("loginName", uNm, max_age=360, path="/")
            self.redirect("/messcenter?user="+uNm)

class MessCenter(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('messcenter.html')
        
        uNm = self.request.get("user")
        template_values = {
            "user": uNm,
            "userList": userList
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
        
        template_values = {
            "user": user,
            "student": student
        }
        
        self.response.write(template.render(template_values))
        
    def post(self):
        pass

app = webapp2.WSGIApplication([
	('/', Login),
	('/messcenter', MessCenter),
	('/chat', Chat)
], debug=True)

userList = parseTxt("accounts.csv")	#r = newR;
