from django.db import models
from django.utils.translation import ugettext_lazy as _
from businesses.models import Business

# Create your models here.

QUESTION_TYPES = (
    ('yn', 'Yes or No'),
    ('sa', 'Short Answer'),
    ('mcsa', 'Multi Choice(Single Answer)'),
    ('ra', 'Rating'),
    ('mcma', 'Multi Choice(Multiple Answer)'),
)


class Option(models.Model):
    text = models.TextField(_("Option text"))

    def __str__(self):
        return self.text


class Question(models.Model):
    title = models.TextField(_("Title"))
    ques_type = models.CharField(_("Ques Type"), max_length=150,
                                 choices=QUESTION_TYPES, default="yn")
    options = models.ManyToManyField(Option)
    business = models.ForeignKey(Business, blank=True, null=True)

    def __str__(self):
        return self.title
