from django.urls import path
from quiz.quiz.views import QuizView
from quiz.question.views import QuestionView
from quiz.attempt.views import AttemptView
from quiz.answer.views import AnswerView, UserAnswerView

urlpatterns = [
    path('questions', QuestionView.as_view(), name='question'),
    path('answer', AnswerView.as_view(), name='questionview'),
    path('user-answer', UserAnswerView.as_view(), name='useranswer')   
]
