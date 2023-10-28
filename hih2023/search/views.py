from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, PasswordChangingForm
from .models import User


def profile_detail(request, username):
    template = 'search/profile.html'
    profile = get_object_or_404(User, username=username)
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def index(request):
    context = {'docs': None}
    template = 'search/index.html'
    if request.method == "POST":
        form = request.POST.dict()
        context['docs'] = form['input_field']
        # print(form['input_field'].value())
        print(form['input_field'])
        return render(request, template, context)
    else:
        return render(request, template)


def registration_view(request):
    template = 'registration/registration_form.html'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search:index')
    else:
        form = RegistrationForm()

    return render(request, template, {'form': form})


@login_required
def change_password(request):
    template = 'registration/password_change_form.html'
    # if request.method == 'POST':
    #     form = CustomPasswordChangeForm(request.user, request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         update_session_auth_hash(request, user)
    #         return redirect('search:profile')
    # else:
    #     form = CustomPasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangingForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        form = PasswordChangingForm(request.user)
    return render(request, template, {'form': form})
