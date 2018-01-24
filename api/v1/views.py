from django.shortcuts import render
from .models import  Average
from .serializers import  AverageSerializer
from rest_framework import viewsets


# Create your views here.


class AverageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Average.objects.order_by('-created')
    serializer_class = AverageSerializer

