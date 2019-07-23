from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import LevelSerializer
from .models import Level

class LevelViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allows levels to be viewed or edited.
    """
    queryset = Level.objects.all()
    serializer_class = LevelSerializer