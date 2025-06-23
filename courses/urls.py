from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
path('<slug:slug>/enroll/', views.enroll, name='enroll'),
    path('<slug:course_slug>/lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('<slug:course_slug>/lesson/<int:lesson_id>/exam/', views.take_exam, name='take_exam'),
    path('<slug:course_slug>/lesson/<int:lesson_id>/exam/submit/', views.submit_exam, name='submit_exam'),
    path('exam/results/<int:submission_id>/', views.exam_result, name='exam_result'),
]