from django.urls import path
from app_sigas import views
from django.views.generic.base import RedirectView

urlpatterns = [
    #acesso e sair
    path('login/',views.login_view,name='login'),
    path('', RedirectView.as_view(url='login', permanent=False)), 
    path('logout/', views.logout_view, name='logout'),

    #Perfils
    path('perfil/',views.perfil,name='perfil'),

    #Pagina inicial
    path('pagina/', views.pagina_inicial, name='pagina_inicial'),

    #Diario
    path('pagina/diario', views.diario, name='diario'),
    path('pagina/diario/<int:disciplina_id>/', views.diario_detalhado, name='diario_detalhado'),
    path('pagina/diario/<int:disciplina_id>/registraraula/', views.registrar_aula, name='registrar_aula'),
    path('pagina/diario/<int:disciplina_id>/registrarfalta/', views.registrar_falta, name='registrar_falta'),
    
    #cadastro
    path('cadastro/',views.cadastro,name='cadastro'),
    path('cadastro/aluno',views.cadastro_aluno,name='cadastro_aluno'),
    path('cadastro/professor',views.cadastro_professor,name='cadastro_professor'),

    #Popular banco de dados (PRATICIDADE)
    path('popularbd/',views.popular_bd,name='popularBd'),
]