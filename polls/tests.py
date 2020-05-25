import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question


# Create your tests here.
class TestQuestionModel(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=23)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, seconds=2)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=2)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), False)
