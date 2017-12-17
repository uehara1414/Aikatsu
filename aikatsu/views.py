from django.conf.urls import url

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def hello_world(request):
    """## Some documentations"""
    return Response({'results': [
        '豪華にする',
        'モチベーションをあげる',
        'すぐに試せる',
        '着る'
    ] * 5})


urlpatterns = [
    url(r'get_verbs', hello_world)
]
