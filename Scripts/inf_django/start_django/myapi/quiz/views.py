from django.shortcuts import render
from rest_framework.responce import Response
from rest_framework.decorates import api_view
from .models import Quiz
from .serializers import QuizSerializer
# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world!")