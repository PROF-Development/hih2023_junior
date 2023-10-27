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


# def profile_detail(request, username):
#     template = 'search/profile.html'
#     profile = get_object_or_404(User, username=username)
#     context = {
#         'profile': profile,
#     }
#
#     return render(request, template, context)
#
#
# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = User
#     template_name = 'registration/password_change_form.html'
#     form_class = RegistrationForm
#
#     def get_object(self, queryset=None):
#         if self.request.user.is_authenticated:
#             profile, created = User.objects.get_or_create(
#                 user=self.request.user
#             )
#             return profile
#
#     def dispatch(self, request, *args, **kwargs):
#         instance = self.get_object()
#         if instance.user == self.request.user:
#             return super().dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         profile = form.save(commit=False)
#         profile.user.username = form.cleaned_data['full_name']
#         profile.user.email = form.cleaned_data['email']
#         profile.user.password = form.cleaned_data['password']
#         profile.user.save()
#         profile.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('search:index')


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

from django.shortcuts import render, redirect
from .forms import RegistrationForm

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

