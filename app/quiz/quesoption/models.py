from django.db import models
from quiz.question.models import Question
from django.core.exceptions import ValidationError

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    option = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        return self.option 
    

