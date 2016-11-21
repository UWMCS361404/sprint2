import webapp2
import jinja2
import os

from user import User
from util import parseTxt
from question import Question
from message import Message

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)

userList = []
class Login(webapp2.RequestHandler):
    error = ""
    def get(self):
        uNm = self.request.cookies.get("CurrentUser")
        if uNm == "":
            template = JINJA_ENVIRONMENT.get_template('login.html')
            template_values = {
                "user": uNm,
                "error": error,
            }
            self.response.write(template.render(template_values))


        else:
            if (getAccount(uNm).aType == 's'):
                self.redirect('/studentcenter')
            else:
                self.redirect('/instructorcenter')

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
            #self.response.set_cookie('name', name, path='/')
            self.response.set_cookie("CurrentUser", uNm, max_age=360, path="/")
            if (getAccount(uNm).aType == 's'):
                self.redirect("/studentcenter")
            else:
                self.redirect("/instructorcenter")

        else:
            error = "enter a valid username and password"


class InstructorCenter(webapp2.RequestHandler):

    QL = Question.query(Question.lec==getAccount(uNm).lec).fetch()

    def get(self):
        uNm = self.request.cookies.get('CurrentUser')
        QL = Question.query(Question.lec==getAccount(uNm).lec).fetch()
        template = JINJA_ENVIRONMENT.get_template('instructorcenter.html')
        uNm = self.request.get("CurrentUser")
        template_values = {
            "CurrentUser": uNm,
            'QL': QL,
        }

    def post(self):
        time = datetime.datetime.now()
        uNm = self.request.cookies.get('CurrentUser')

    # def goToChat(self):
    #
    #     template_values = {
    #         'user'
    #     }






# class StudentCenter(webapp2.RequestHandler):
#     def get(self):
#     def post(self):


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

class Test(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('test.html')
        test1 = "test 1, make sure this is running"
        test2 = "test 2, and loading template vals"
        template_values = {
            "test1": test1,
            "test2": test2
        }
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
	('/', Login),
#    ('/studentcenter'), StudentCenter),
    ('/instructorcenter'), InstructorCenter,
	('/test', Test),
	('/chat', Chat)
], debug=True)

userList = parseTxt("accounts.csv")
