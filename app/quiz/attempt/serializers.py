from rest_framework import serializers
from .models import Attempt

from rest_framework import serializers
from .models import Attempt

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = '__all__'

    def create(self, validated_data):
        attempt = Attempt.objects.create(
            user_id=validated_data.get('user_id'),
            quiz_id=validated_data.get('quiz_id'),
            start_time=validated_data.get('start_time'),
            end_time=validated_data.get('end_time'),
            score=validated_data.get('score')
        )
        return attempt
