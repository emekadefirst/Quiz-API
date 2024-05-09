from django.db import models

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    description = models.TextField(default=None)
    duration = models.TimeField()
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.quiz_id