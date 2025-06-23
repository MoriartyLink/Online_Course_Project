from django.contrib import admin
from .models import Course, Lesson, Question, Choice, ExamSubmission, Answer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'lesson', 'points')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')

class AnswerInline(admin.TabularInline):
    model = Answer
    readonly_fields = ('question', 'selected_choice', 'is_correct')
    extra = 0

class ExamSubmissionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('student', 'lesson', 'score', 'submitted_at')

admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(ExamSubmission, ExamSubmissionAdmin)
admin.site.register(Answer)