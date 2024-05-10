from django import forms
from .models import Answer
from quiz.answer.models import QuestionOption

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question_option', 'is_correct']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit the queryset for question_option field to options associated with the question
        if 'question' in self.initial:
            question = self.initial['question']
            self.fields['question_option'].queryset = QuestionOption.objects.filter(question=question)


