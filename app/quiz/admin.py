from django.contrib import admin
from quiz.quiz.models import Quiz
from quiz.question.models import Question
from quiz.attempt.models import Attempt 
from quiz.answer.models import Answer, UserAnswer
from quiz.question.options import QuestionOption
from quiz.quesoption.models import Option

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'name', 'description', 'duration', 'is_active')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'quiz', 'question')
    list_filter = ('quiz',)
    search_fields = ('question',)

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 4

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('question_option__option',)

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    # inlines = [AnswerInline]
    list_display = ('question', 'option')

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'question', 'selected_answer', 'is_correct')
    list_filter = ('user_id', 'question__quiz')
    search_fields = ('user__username', 'question__question')
