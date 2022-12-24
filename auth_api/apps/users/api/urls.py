from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, RefreshView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('get_auth_token', RefreshView.as_view()),
    path('logout', LogoutView.as_view()),
    path('users', UserView.as_view()),
]
