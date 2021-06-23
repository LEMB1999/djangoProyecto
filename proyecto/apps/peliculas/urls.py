# peliculas/urls.py
from django.urls import path
from .views import HomePageView,Perfil,Login,Logout,Signup
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("home",login_required(HomePageView.as_view()), name='home'),
    path("perfil",login_required(Perfil.as_view()), name="perfil"),
    path("singup",login_required(Signup.as_view()),name="singup"),
    path("accounts/login",Login.as_view(),name="login"),
    path("",Login.as_view()),
    path("logout",Logout,name="logout")
]