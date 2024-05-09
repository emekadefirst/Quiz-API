from django.db import models
from quiz.quiz.models import Quiz
from django.utils import timezone

class Question(models.Model):
    QUESTION_TYPE = (
        ('multichoice', 'Multichoice'),
        ('german', 'German'),
    )
    question_id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(default=None)
    created_at = models.DateTimeField(default=timezone.now)
    question_type = models.CharField(
        max_length=13,
        choices=QUESTION_TYPE,
        default='multichoice',
    )
    
    class Meta:
        ordering = ['-created_at']
    
    
    def __str__(self):
        return self.question + str(self.question_type)
