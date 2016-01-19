from django.views import generic
from .forms import *
from .models import *

# Create your views here.
from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView


class ContactWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


class SurveyView(generic.View):

    def get(self, request, *args, **kwargs):
        kwargs["survey"] = Survey.objects.get(pk=self.kwargs["survey_id"])
        return render_to_response("survey.html", kwargs)

    def post(self, request, *args, **kwargs):
        print request.POST["1"]


class SurveyAll(generic.ListView):

    model = Survey
    template_name = "survey_all.html"


class Home(generic.TemplateView):

    template_name = "home.html"
