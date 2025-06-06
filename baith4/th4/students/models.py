# students/models.py
from django.db import models

class Student(models.Model):
    KHOA_CHOICES = [
        ('cntt', 'Công nghệ thông tin'),
        ('ck', 'Cơ khí'),
        ('dt', 'Điện tử'),
    ]

    ho_ten = models.CharField(max_length=100)
    mssv = models.CharField(max_length=20)
    email = models.EmailField()
    khoa = models.CharField(max_length=10, choices=KHOA_CHOICES)
    math = models.FloatField()
    physics = models.FloatField()
    chemistry = models.FloatField()

    def __str__(self):
        return f"{self.ho_ten} - {self.mssv}"
