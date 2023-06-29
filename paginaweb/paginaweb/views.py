from django.shortcuts import render

def index(request):
        return render(request, 'index.html')

def usuarios(request):
        nombres = ['Juan', 'María', 'Pedro']
        return render(request, 'usuarios.html', {'nombres': nombres})