from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return render(request, 'closet/index.html', {})

def login(request):
    return render(request, 'closet/login.html', {})

def login_form(request):
    return render(request, 'closet/login_form.html', {})

def cadastro_de_roupas(request):
    return render(request, 'closet/cadastro_de_roupas.html', {})

def create(request):
    return render(request, 'closet/login_form.html',{})

def menu(request):
    return render(request, 'closet/menu.html', {})

def menu_cadastros(request):
    return render(request, 'closet/menu_cadastros.html', {})

def cadastro_tipos(request):
    return render(request, 'closet/cadastro_tipos.html', {})

def cores(request):
    return render(request, 'closet/cores.html', {})

def marcas(request):
    return render(request, 'closet/marcas.html', {})

def estacao(request):
    return render(request, 'closet/estacao.html', {})

def tecidos(request):
    return render(request, 'closet/tecidos.html', {})

def estilos(request):
    return render(request, 'closet/estilos.html', {})

def tamanhos(request):
    return render(request, 'closet/tamanhos.html', {})

def funcoes(request):
    return render(request, 'closet/funcoes.html', {})

def visualizar_roupas(request):
    return render(request, 'closet/visualizar_roupas.html', {})

def indicar_roupas(request):
    return render(request, 'closet/indicar_roupas.html', {})

def doar_roupas(request):
    return render(request, 'closet/doar_roupas.html', {})

def login_form_2(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha não batem!'
    return render(request, 'closet/login_form.html', data)
    
@require_POST
def cadastrar_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux:
            return render(request, 'closet/index.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})
    except User.DoesNotExist:
        nome_usuario = request.POST['name']
        email = request.POST['email']
        senha = request.POST['password']

        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()
        return render(request, 'closet/login_form.html',{('msg: Usuário cadastrado com sucesso!')})

@require_POST
def entrar(request):
    usuario_aux = User.objects.get(email=request.POST['email'])
    usuario = authenticate(username=usuario_aux.username,
                           password=request.POST["senha"])
    if usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('closet/index.html')

    return HttpResponseRedirect('closet/menu.html')

@require_POST
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid login credentials'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})