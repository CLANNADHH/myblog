from django.urls import path

from userprofile.views import UserLoginView

app_name = "userprofile"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login")
]


