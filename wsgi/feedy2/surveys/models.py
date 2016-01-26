from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from businesses.models import Business
from questions.models import Question
from customers.models import Customer
from jsonfield import JSONField
# Create your models here.


class Survey(models.Model):
    title = models.CharField(_("Title"), max_length=150)
    business = models.ForeignKey(Business)
    questions = models.ManyToManyField(Question)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SurveyRecord(models.Model):
    survey = models.ForeignKey(Survey)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    answers = JSONField(blank=True, null=True)
    bill_number = models.CharField(
        _("Bill Number"), max_length=150, null=True, blank=True)
    email_id = models.EmailField(_("Email"), blank=True, null=True)
    mobile = models.CharField(
        _("Mobile"), blank=True, null=True, max_length=150)
    date_added = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.survey.title + "'s Record"
