from django import forms
from django.contrib.auth.models import User


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

