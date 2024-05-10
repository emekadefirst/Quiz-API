#Generate secret keys

#Run "./manage.py shell" or "python manage.py shell" from django.core.management.utils import get_random_secret_key print(get_random_secret_key())

{ "username": "test_user", "password": "test_password", "email": "test@example.com" }

./manage.py makemigrations api --empty Migrations for 'api': api\migrations\0001_initial.py


So this is what i want for this option model
class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    option_a = models.CharField(max_length=200, null=True, blank=True, default=None)
    option_b = models.CharField(max_length=200, null=True, blank=True, default=None)
    option_c = models.CharField(max_length=200, null=True, blank=True, default=None)
    option_d = models.CharField(max_length=200, null=True, blank=True, default=None)
    
    
    def __str__(self):
        return f'{self.option_a} {self.option_b} {self.option_c} {self.option_d}'
via the admin when i want to create and answer to the question i want to be able to select from the options as the answer and not all option available,
I think it's the function that is causing it