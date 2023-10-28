from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required, permission_required

from .forms import RegistrationForm, PasswordChangingForm
from .models import User, UserProfile

from django.contrib.auth import login
from .forms import RegistrationForm
from .models import User
from django.http import FileResponse, Http404, HttpResponse

# import models as model
import search.processing_modules as function


def profile_detail(request, username):
    template = 'search/profile.html'
    profile = get_object_or_404(User, username=username)
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def index(request):
    context = {"documents": None}
    template = 'search/index.html'
    if request.method == "POST":
        req_dict = request.POST.dict()
        context["documents"] = function.get_documents(req_dict)

    return render(request, template, context)


# Does not work properly at the moment
def viewer(request):
    if request.method == 'GET':
        filename = request.GET.get('id', '')
        application = filename.split('.')[-1]

        try:
            return FileResponse(open(f'data/files/{filename}', 'rb'), content_type=f'application/{application}')
        except FileNotFoundError:
            raise Http404()


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
    if request.method == "POST":
        form = PasswordChangingForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        form = PasswordChangingForm(request.user)
    return render(request, template, {'form': form})


def is_verified_user(user):
    if user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=user)
            return user_profile.roles == 'verified' or user.is_superuser
        except UserProfile.DoesNotExist:
            return False
    return False
