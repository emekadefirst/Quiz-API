from django.shortcuts import get_object_or_404
from .serializers import AnswerSerializer, UserAnswerSerializer
from .models import Answer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AnswerView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Answer, pk=pk, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        answer = Answer.objects.all()
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserAnswerView(APIView):
    def post(self, request, format=None):
        serializer = UserAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

