from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['ho_ten', 'mssv', 'email', 'khoa', 'math', 'physics', 'chemistry']
        widgets = {
            'ho_ten': forms.TextInput(attrs={'class': 'form-control'}),
            'mssv': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập email sinh viên'}),
            'khoa': forms.Select(attrs={'class': 'form-control'}),
            'math': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 10}),
            'physics': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 10}),
            'chemistry': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 10}),
        }

class SurveyForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác'),
    ]

    HOBBY_CHOICES = [
        ('reading', 'Đọc sách'),
        ('traveling', 'Du lịch'),
        ('sports', 'Thể thao'),
        ('music', 'Nghe nhạc'),
    ]

    ho_ten = forms.CharField(
        label="Họ tên",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    gioi_tinh = forms.ChoiceField(
        label="Giới tính",
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect
    )

    so_thich = forms.MultipleChoiceField(
        label="Sở thích",
        choices=HOBBY_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    ngay_sinh = forms.DateField(
        label="Ngày sinh",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    nhan_tin = forms.BooleanField(
        label="Đăng ký nhận tin?",
        required=False
    )

class UserRegisterForm(forms.Form):
    BANNED_USERNAMES = ['admin', 'root', 'test', 'superuser']

    username = forms.CharField(
        label="Tên đăng nhập",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        label="Mật khẩu",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    confirm_password = forms.CharField(
        label="Nhập lại mật khẩu",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username.lower() in self.BANNED_USERNAMES:
            raise forms.ValidationError("Tên đăng nhập không được phép.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith("@student.edu.vn"):
            raise forms.ValidationError("Email phải có đuôi @student.edu.vn.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if password and confirm and password != confirm:
            self.add_error("confirm_password", "Mật khẩu nhập lại không khớp.")

            
# class StudentForm(forms.Form):
#     HO_TEN_LABEL = "Họ và tên"
#     MSSV_LABEL = "Mã số sinh viên"
#     EMAIL_LABEL = "Email"
#     KHOA_LABEL = "Khoa"

#     KHOA_CHOICES = [
#         ('cntt', 'Công nghệ thông tin'),
#         ('ck', 'Cơ khí'),
#         ('dt', 'Điện tử'),
#     ]

#     ho_ten = forms.CharField(
#         label=HO_TEN_LABEL,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     mssv = forms.CharField(
#         label=MSSV_LABEL,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     email = forms.EmailField(
#         label=EMAIL_LABEL,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Nhập email sinh viên',
#             'class': 'form-control'
#         })
#     )
#     khoa = forms.ChoiceField(
#         label=KHOA_LABEL,
#         choices=KHOA_CHOICES,
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )