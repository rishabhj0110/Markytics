from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
# app_name = 'userApp'

urlpatterns = [
    path('', TemplateView.as_view(template_name='userApp/landingPage.html'), name='landingPage'),
    path('login/', LoginView.as_view(template_name= 'userApp/login.html'), name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register', views.userRegister, name='register'),
    path('home/', views.home, name='home'),
    path('report/', views.reportIncident, name='reportIncident'),
    
]