from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.UserSignUpView.as_view(), name="user_signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path('token/refresh/', views.CustomTokenRefreshView.as_view(),
         name='token_refresh'),
]
