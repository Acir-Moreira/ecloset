from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('login_form', views.login_form, name='login_form'),
    path('cadastro_de_roupas', views.cadastro_de_roupas, name='cadastro_de_roupas'),
    path('create', views.create, name='create'),
    path('login_form', views.login_form_2, name='login_form'),
    path('cadastrar_usuario', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('menu', views.menu, name='menu'),
    path('menu_cadastros', views.menu_cadastros, name='menu_cadastros'),
    path('cadastro_tipos', views.cadastro_tipos, name='cadastro_tipos'),
    path('cores', views.cores, name='cores'),
    path('marcas', views.marcas, name='marcas'),
    path('estacao', views.estacao, name='estacao'),
    path('tecidos', views.tecidos, name='tecidos'),
    path('estilos', views.estilos, name='estilos'),
    path('tamanhos', views.tamanhos, name='tamanhos'),
    path('funcoes', views.funcoes, name='funcoes'),
    path('visualizar_roupas', views.visualizar_roupas, name='visualizar_roupas'),
    path('indicar_roupas', views.indicar_roupas, name='indicar_roupas'),
    path('doar_roupas', views.doar_roupas, name='doar_roupas'),
    path('entrar', views.entrar, name='entrar'),
]