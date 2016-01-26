from django.conf.urls import url
from views import SurveyView, SurveyAll, Home

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^survey/$', SurveyAll.as_view(), name='survey_all'),
    url(r'^survey/(?P<survey_id>\w+)$', SurveyView.as_view(), name='survey'),
]
