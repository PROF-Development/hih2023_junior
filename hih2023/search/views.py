from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import User

# import models as model
import search.processing_modules as function


def index(request):
    context = {"documents": None}
    template = 'search/index.html'
    if request.method == "POST":
        req_dict = request.POST.dict()
        context["documents"] = function.get_documents(req_dict)
        print(req_dict)

    return render(request, template, context)



def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Логиним пользователя после успешной регистрации
            from django.contrib.auth import login
            login(request, user)

    else:
        form = RegistrationForm()

    return render(request, 'registration/registration_form.html', {'form': form})
