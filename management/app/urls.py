from django.urls import path 
from .views.user import SignupView,LoginView,UserView

urlpatterns = [
    path('users/signup',SignupView.as_view()),
    path('users/login',LoginView.as_view()),
    path('users/profile',UserView.as_view()),
]