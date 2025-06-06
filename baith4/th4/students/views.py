# students/views.py
from django.shortcuts import render
from .forms import StudentForm, SurveyForm, UserRegisterForm

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'students/result.html', {'data': data})
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form})

def student_score_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            avg = (student.math + student.physics + student.chemistry) / 3
            if avg >= 8.0:
                grade = "Giỏi"
            elif avg >= 6.5:
                grade = "Khá"
            elif avg >= 5.0:
                grade = "Trung bình"
            else:
                grade = "Yếu"
            context = {
                'student': student,
                'average': round(avg, 2),
                'grade': grade
            }
            return render(request, 'students/score_result.html', context)
    else:
        form = StudentForm()
    return render(request, 'students/score_form.html', {'form': form})


def user_survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'students/survey_result.html', {'data': data})
    else:
        form = SurveyForm()
    return render(request, 'students/survey_form.html', {'form': form})

def register_user_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            return render(request, 'students/register_success.html', {'data': form.cleaned_data})
    else:
        form = UserRegisterForm()
    return render(request, 'students/register_form.html', {'form': form})