from django.db import models
from quiz.quiz.models import Quiz

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(default=None)

    def __str__(self):
        return f'{self.question} {self.quiz}'




