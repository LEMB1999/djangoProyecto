from django.views.generic import TemplateView
from .models import Pelicula
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

class HomePageView(TemplateView):
    peliculas = Pelicula.objects.all()
    template_name="home.html"

    def get_context_data(self,*args,**kwargs):
        context = super(HomePageView,self).get_context_data(*args,**kwargs)
        context["peliculas"] = self.peliculas
        return context

class Perfil(TemplateView):
    template_name="perfil.html"


class Signup(TemplateView):
    template_name = "signup.html"
    # user correo contraseña
    def post(self,request):
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username,email,password)
        user.firstname = name
        user.save()
        return HttpResponseRedirect(reverse('login'))
    


class Login(TemplateView):
    template_name="login.html"
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('login'))     


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))     