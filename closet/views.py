from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'closet/index.html', {})

def login(request):
    return render(request, 'closet/login.html', {})

def login_form(request):
    return render(request, 'closet/login_form.html', {})

def cadastro_de_roupas(request):
    return render(request, 'closet/cadastro_de_roupas.html', {})
