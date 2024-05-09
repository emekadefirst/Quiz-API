from django.db import models
from django.contrib.auth.models import User
from quiz.quiz.models import Quiz
from django.utils import timezone

class Attempt(models.Model):
    attempt_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    score = models.FloatField()
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.attempt_id} {self.user_id} {self.score}'