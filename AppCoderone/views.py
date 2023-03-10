from django.shortcuts import render
from django.http import HttpResponse
from AppCoderone.models import Curso
# Create your views here.

def curso(request):
    return render(request, "index.html")
def estudiantes(request):
    return render(request, "index.html")
def profesores(request):
    return render(request, "index.html")