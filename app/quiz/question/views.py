import random
from hashlib import sha256
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
        user_id = request.user.id  # Assuming user ID is used as a unique identifier
        shuffled_questions = self.shuffle_questions(user_id, questions)
        questions_subset = shuffled_questions[:35]  # Limiting to 35 questions
        serializer = QuestionSerializer(questions_subset, many=True)
        return Response(serializer.data)

    def shuffle_questions(self, user_id, questions):
        # Generate a unique seed for shuffling based on user ID and a secret key
        secret_key = "your_secret_key"  # Change this to your secret key
        seed = sha256(f"{user_id}-{secret_key}".encode()).hexdigest()
        random.seed(seed)

        # Shuffle the questions
        shuffled_questions = list(questions)
        random.shuffle(shuffled_questions)

        return shuffled_questions

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
