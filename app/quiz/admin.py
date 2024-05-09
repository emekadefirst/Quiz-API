from django.contrib import admin
from quiz.quiz.models import Quiz
from quiz.question.models import Question
from quiz.attempt.models import Attempt 
from quiz.answer.models import Answer, UserAnswer

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'description', 'duration', 'is_active')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question', 'quiz', 'created_at', 'question_type')
    list_filter = ('quiz', 'question_type')
    search_fields = ('question',)

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('attempt_id', 'user_id', 'quiz_id', 'start_time', 'end_time', 'created_at', 'score')
    list_filter = ('quiz_id',)
    search_fields = ('user_id__username',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'question', 'answer_text', 'is_correct')
    list_filter = ('question', 'is_correct')
    search_fields = ('answer_text',)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'is_correct')
    list_filter = ('user', 'question__quiz')
    search_fields = ('user__username', 'question__question')

