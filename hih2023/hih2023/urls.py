from django.contrib import admin
from django.urls import path, include

from search.views import registration_view, change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls', namespace='search')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', registration_view, name='registration'),
    path('change_password/', change_password, name='change_password'),
]
