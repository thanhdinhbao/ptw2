# student_info/urls.py
from django.urls import path
from .views import save_students_json, view_students_json

urlpatterns = [
    path('save-students/', save_students_json, name='save_students'),
    path('view-students/', view_students_json, name='view_students'),
]
