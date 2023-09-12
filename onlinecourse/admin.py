from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

"""Choices class"""
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

"""Questions class"""
class QuestionInline(admin.StackedInline):
    models = Question
    extra = 2

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

"""Question admin, adding question to lessons"""
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
