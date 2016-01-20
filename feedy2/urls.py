"""feedy2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from surveys.forms import ContactForm1, ContactForm2
from surveys.views import ContactWizard
from surveys import urls as survey_urls
from rest_framework.routers import DefaultRouter
from rest_api.views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import JqmTest

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2])),
    url(r'', include(survey_urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^jqmtest/', JqmTest.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
