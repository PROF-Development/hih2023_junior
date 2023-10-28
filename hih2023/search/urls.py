from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>/', views.profile_detail, name='profile'),
]
