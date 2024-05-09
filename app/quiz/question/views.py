from django.shortcuts import get_object_or_404
from .serializers import QuestionSerializer
from .models import Question
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class QuestionView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Question, pk=pk)

    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    