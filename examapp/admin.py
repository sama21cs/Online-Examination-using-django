from django.contrib import admin
from .models import Test, Question, UserResponse, Feedback

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'total_questions', 'total_marks']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'test', 'is_mcq']

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['user', 'test', 'question', 'is_correct', 'marked_for_review']
    list_filter = ['test', 'is_correct', 'marked_for_review']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'test', 'rating', 'timestamp']