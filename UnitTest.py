import unittest
import message
import user
import datetime
import util
import os
import webapp2
import jinja2
from google.appengine.ext import ndb

class Sprint1Tests(unittest.TestCase):
    def setUp(self):
        Users = parseTxt("testaccnts.txt")
        message = Message(sName="Jim", rName="Fred", time=datetime.datetime(2009,9,1,12,43,1), content="first message")
        message.put()
        message = Message(sName="Fred", rName="Jim", time=datetime.datetime(2009,9,9,1,4,1), content="third message")
        message.put()
        message = Message(sName="Bob", rName="Fred", time=datetime.datetime(2009,9,3,5,4,1), content="second message")
        message.put()
        self.Messages = Message.all
    def tear(self):
        self.Messages = Message.all()
        for M in Messages:
            M.key.delete()
        del Users
    def UsersCopy(self):
        self.Users.append(User(name="Kyle",password="asdf",aType="i"))
        self.assertEqual

    def nameFunctions(self):
        self.assertEqual(self.Users[0].name, "Jim")
        self.Users[0].setName("Jack")
        self.assertEqual(self.Users[0].name, "Jack")
        self.assertEqual(self.Users[0].getName(), "Jack")

    def passwordFunctions(self):
        self.assertEqual(self.Users[0].pwd, "123")
        self.Users[0].setName("asd")
        self.assertEqual(self.Users[0].pwd, "asd")
        self.assertEqual(self.Users[0].getPwd(), "asd")

    def aTypeFunctions(self):
        self.assertEqual(self.Users[0].aType, "s")
        self.Users[0].setaType("i")
        self.assertEqual(self.Users[0].aType, "i")
        self.assertEqual(self.Users[0].getaType(), "i")

    def messageFunctions(self):
        self.Messages = self.Messages.order('-date')
        self.assertEqual(self.Messages[0].content, "first message")
        self.assertEqual(self.Messages[1].content, "second message")
        self.assertEqual(self.Messages[2].content, "third message")

suite = unittest.TestLoader().loadTestsFromTestCase(Sprint1Tests)
unittest.TextTestRunner(verbosity=2).run(suite)
