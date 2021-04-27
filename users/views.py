from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from allauth.account.views import SignupView, LoginView

# class MySignUpView(SignupView):
#     template_name = 'users/signup.html'


# class MyLoginView(LoginView):
#     template_name = 'users/login.html'
