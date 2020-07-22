from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup")
]