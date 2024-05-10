from django.urls import path
from quiz.quiz.views import QuizView
from quiz.question.views import QuestionView
from quiz.attempt.views import AttemptView
from quiz.auth.views import LoginUser, RegisterUser
from quiz.answer.views import AnswerView, UserAnswerView

urlpatterns = [
    path('question', QuestionView.as_view(), name='question'),
    path('answer', AnswerView.as_view(), name='questionview'),
    path('user-answer', UserAnswerView.as_view(), name='useranswer'),
    path('attempt', AttemptView.as_view(), name='attempt'),    
    path('quiz', QuizView.as_view(), name='quiz'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
]
