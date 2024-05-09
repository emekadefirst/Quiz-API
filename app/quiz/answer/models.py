from django.db import models
from django.contrib.auth.models import User
from quiz.question.models import Question

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    is_correct = models.BooleanField(default=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(default=None)
    
    def __str__(self):
        return f'{self.answer_text}, Correct: {self.is_correct}'

class UserAnswer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'User: {self.user_id}, Question: {self.question}, Answer: {self.answer_id}'
