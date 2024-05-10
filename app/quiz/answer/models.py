from django.db import models
from django.contrib.auth.models import User
from quiz.question.options import QuestionOption
from quiz.question.models import Question
from quiz.quesoption.models import Option

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'Correct: {self.is_correct}, {self.option}'




class UserAnswer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'User: {self.user_id}, Question: {self.question}, Answer: {self.selected_answer}'

