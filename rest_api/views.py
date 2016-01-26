from rest_framework import viewsets
from surveys.models import Survey
from serializers import *


class SurveyViewSet(viewsets.ReadOnlyModelViewSet):

    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
