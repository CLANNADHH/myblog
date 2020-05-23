from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

from userprofile.forms import UserLoginForm


class UserLoginView(LoginView):
    template_name = "usersprofile/login.html"
    next_page = "article:article_list"
    form_class = UserLoginForm
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = "article:article_list"
