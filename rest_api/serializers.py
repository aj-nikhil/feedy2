from rest_framework import serializers
from surveys.models import Survey


class SurveySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Survey
        fields = ('questions')
