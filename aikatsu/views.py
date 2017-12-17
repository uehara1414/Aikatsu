from django.conf.urls import url

from rest_framework.response import Response
from rest_framework.decorators import api_view

from aikatsu.models import Verb
import random


@api_view(['GET'])
def hello_world(request):
    """## Some documentations"""
    verbs = random.choices(Verb.objects.all(), k=10)
    return Response({'results': [verb.word for verb in verbs]})


urlpatterns = [
    url(r'get_verbs', hello_world)
]
