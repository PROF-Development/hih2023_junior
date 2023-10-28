from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/registration/', views.registration_view, name='registration'),
    path('viewer/', views.viewer, name='viewer'),
]
