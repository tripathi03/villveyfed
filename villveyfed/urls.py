
import django.contrib.auth.views
from django.urls import path, include
from .views import show_register_page
from django.contrib import admin
from django.urls import path
from memdcs import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", django.contrib.auth.views.LoginView.as_view()),
    path("logout/", django.contrib.auth.views.LogoutView.as_view()),
    path("register/", show_register_page),
    path("application/", include(urls))
]
