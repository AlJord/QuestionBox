from django.shortcuts import render
from api.models import Question, Answer, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import QuestionSerializer, QuestionAnswerSerializer

class QuestionListView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserQuestionsListView(ListAPIView):
    queryset = User.questions.all()
    serializer_class = QuestionSerializer

class QuestionDetailsView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionAnswerSerializer

