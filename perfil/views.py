from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render

class CriarPerfil(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'criar_perfil.html')

class Update(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'update.html')

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

class Logout(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'logout.html')

