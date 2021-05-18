from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializes import QuizSerializer
import random
# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world!")

@api_view(['POST'])
def randomQuiz(request,id):
    totalQuizs=Quiz.objects.all()
    randomQuizs=random.sample(list(totalQuizs),id)
    serializer=QuizSeiralizer(randomQuizs,many=True)
    return Response(Serializer.data)