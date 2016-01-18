from __future__ import unicode_literals

from django.db import models
from businesses.models import Business
from questions.models import Question
from customers.models import Customer
# Create your models here.


class Survey(models.Model):
    business = models.ForeignKey(Business)
    questions = models.ManyToManyField(Question)
    date_added = models.DateField(auto_now=True)


class SurveyRecord(models.Model):
    survey = models.ForeignKey(Survey)
    customer = models.ForeignKey(Customer)
