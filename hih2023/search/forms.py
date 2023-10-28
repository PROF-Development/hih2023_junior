from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm


class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, help_text="Обязательное поле.")
    email = forms.EmailField(required=True, help_text="Обязательное поле.")
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text="Обязательное поле.")

    def save(self):
        full_name = self.cleaned_data['full_name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = full_name
        user.save()
        return user


class CustomPasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(
        label="Старый пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    confirm_new_password = forms.CharField(
        label="Подтвердите новый пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
