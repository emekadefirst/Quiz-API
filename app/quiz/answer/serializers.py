from rest_framework import serializers
from .models import Answer, UserAnswer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        answer = Answer.objects.create(
            is_correct=validated_data['is_correct'],
            question=validated_data['is_correct'],
            answer_text=validated_data['answer_text']
        )
        return answer


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'


    def create(self, validated_data):
        user_answer = UserAnswer.objects.create(
            user=validated_data.get('user'),
            is_correct=validated_data.get('is_correct'),
            question=validated_data.get('question'),
            answer=validated_data.get('answer')
        )
        return user_answer
