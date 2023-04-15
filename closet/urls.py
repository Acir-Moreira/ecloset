from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('login_form', views.login_form, name='login_form'),
    path('cadastro_de_roupas', views.cadastro_de_roupas, name='cadastro_de_roupas'),

]