import json
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

def save_students_json(request):
    students = [
        {"id": 1, "name": "Nguyen Van A", "major": "Công nghệ thông tin", "gpa": 3.5},
        {"id": 2, "name": "Tran Thi B", "major": "Kinh tế", "gpa": 3.8},
        {"id": 3, "name": "Le Van C", "major": "Cơ khí", "gpa": 2.9},
        {"id": 4, "name": "Pham Thi D", "major": "Điện tử", "gpa": 3.2},
        {"id": 5, "name": "Hoang Van E", "major": "Quản trị", "gpa": 3.6},
    ]

    json_path = os.path.join(settings.MEDIA_ROOT, 'json', 'students.json')
    os.makedirs(os.path.dirname(json_path), exist_ok=True)

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

    return HttpResponse("Đã lưu file students.json thành công!")

def view_students_json(request):
    json_path = os.path.join(settings.MEDIA_ROOT, 'json', 'students.json')

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            students = json.load(f)
    except FileNotFoundError:
        return HttpResponse("File students.json chưa tồn tại.")

    return render(request, 'student_info/students_list.html', {'students': students})