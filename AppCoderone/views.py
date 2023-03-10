from django.shortcuts import render
from django.http import HttpResponse
from AppCoderone.models import Curso
# Create your views here.

def cursos(request):
    all_cursos = Curso.objects.all()
    context = {"cursos": all_cursos}
    return render(request, "AppCoderone/cursos.html", context=context)

def crear_curso(request, nombre, camada):
    save_curso=Curso(nombre=nombre, camada= int(camada))
    save_curso.save()
    context= {"nombre": nombre}
    return render(request, "AppCoderone/save_curso.html", context=context)
def estudiantes(request):
    return render(request, "AppCoderone/estudiantes.html")
def profesores(request):
    return render(request, "AppCoderone/profesores.html")