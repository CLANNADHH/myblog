from django.urls import path

from userprofile.views import UserLoginView, UserLogoutView

app_name = "userprofile"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]


