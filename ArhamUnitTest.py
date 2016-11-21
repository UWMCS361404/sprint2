import unittest
import message
import question
import datetime
import util
import os
import webapp2
import jinja2
from google.appengine.ext import ndb

class QuestionTests(unittest.TestCase):
    def setUp(self):
        question = Question(owner = "Arham",topic="When is class starting?", answered = True, messages = ["Its my first day of class, so i was wondering when is class starting?", "Its at 9 AM."])
        question.put()
         question = Question(owner = "Joe",topic="Is there a late policy?", answered = False, messages = ["Will i get credit for turning stuff in late?"])
        question.put()
        self.Question = Question.all
    def tear(self):
        self.Questions = Question.all()
        for Q in Question:
            Question.key.delete()
        del Users
    def checkOwner(self):
        self.assertEqual(self.Question[0].getOwner,"Arham")
        self.assertFalse(self.Question[0].getOwner,"Joe")
        self.assertTrue(self.Question[1].getOwner,"Joe")
    
    def setOwnerFunctions(self):
        self.assertEqual(self.Question[0].owner, "Arham")
        self.Question[0].setName("Kyle")
        self.assertEqual(self.Question[0].owner, "Kyle")
        self.assertEqual(self.Question[0].getOwner(), "Kyle")
        self.assertFalse(self.Question[0].getOwner,"Joe")
        self.assertTrue(self.Question[1].getOwner,"Joe")
    
    def topicFunctions(self):
        self.assertEqual(self.Question[0].topic, "When is clss starting?")
        self.Question[0].setName("Is there a holiday soon?")
        self.assertEqual(self.Question[0].topic, "Is there a holiday soon?")
        self.assertEqual(self.Question[0].getTopic(), "Is there a holiday soon?")
        self.assertFalse(self.Question[1].getTopic(), "Is there a holiday soon?")
        self.assertTrue(self.Question[1].getTopic(), "Is there a late policy?")
    
   
    def answeredFunctions(self):
        self.assertEqual(self.Question[0].answered, True)
        self.Question[0].setaType(False)
        self.assertEqual(self.Question[0].answered, False)
        self.assertEqual(self.Question[0].getAnswered(), False)
        self.assertTrue(self.Question[1].getAnswered(), False)

    def MessageFunctions(self):
        self.assertEqual(self.Question[0].getMessage, "Its my first day of class, so i was wondering when is class starting?", "Its at 9 AM." )
        self.Question[0].setMessage("This is dumb")
        #self.assertEqual(self.Question[0].messages[last element?], "This is dumb")
        #self.assertEqual(self.Question[0].get(), "This is dumb")

    def getSizeFunctions(self):
        self.assertEqual(self.Question[0].getMessage.size?


suite = unittest.TestLoader().loadTestsFromTestCase(QuestionTests)
unittest.TextTestRunner(verbosity=2).run(suite)
