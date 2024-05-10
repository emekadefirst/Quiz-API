from django.db import models
from .models import Question

class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    option = models.CharField(max_length=200, null=True, blank=True, default=None)

    
    def __str__(self):
        return self.option
   


    
