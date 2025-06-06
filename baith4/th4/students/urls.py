from django.urls import path
from .views import *

urlpatterns = [
    path('student-form/', student_form_view, name='student_form'),
    path('student-score/', student_score_view, name='student_score'),
    path('user-survey/', user_survey_view, name='user_survey'),
    path('register/', register_user_view, name='user_register'),
]