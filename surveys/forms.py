from django import forms
from surveys.models import Survey
from django.forms import ModelForm


class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()


class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ['business', 'questions']
