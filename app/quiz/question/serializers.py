from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        
def create(self, validated_data):
    question = Question.objects.create(
        quiz=validated_data['quiz'],
        question=validated_data['question'],
        question_type=validated_data['question_type']
    )
    return question
