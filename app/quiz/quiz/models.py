from django.db import models

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default=None)
    description = models.TextField(default=None)
    duration = models.TimeField()
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description