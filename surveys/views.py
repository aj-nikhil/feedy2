from django.views import generic
from .models import *
from django.template.context import RequestContext
from django.http import JsonResponse
import itertools

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
        survey = Survey.objects.get(pk=self.kwargs["survey_id"])
        kwargs["survey"] = survey
        self.survey = survey
        return render_to_response("survey.html", kwargs,
                                  context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        resp_dict = {}
        try:
            bill_number = request.POST["bill_number"]
            email = request.POST["email"]
            mobile = request.POST["mobile"]
            meta_data = [
                "bill_number", "mobile", "email", "csrfmiddlewaretoken"]
            post_dict = dict(request.POST.iterlists())
            for k in meta_data:
                post_dict.pop(k, None)
            survey_rec_obj = SurveyRecord(
                bill_number=bill_number, email=email, mobile=mobile)
            survey_rec_obj.answers_json = post_dict
            survey_rec_obj.survey = self.survey
            survey_rec_obj.save()
            resp_dict["status"] = 1
        except Exception as e:
            resp_dict["status"] = 0
            resp_dict["exception"] = e
        return JsonResponse(resp_dict)


class SurveyAll(generic.ListView):

    model = Survey
    template_name = "survey_all.html"


class Home(generic.TemplateView):

    template_name = "home.html"
