from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render

class Pagar(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'pagar.html')

class FecharPedido(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'finalizar.html')

class Detalhe(View):
    pass


