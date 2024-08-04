from django.urls import path
from app_sigas import views
from django.views.generic.base import RedirectView

app_name = 'app_sigas'  # Define o namespace para esta aplicação

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
    path('pagina/diario/<int:disciplina_id>/registrar-aula/', views.registrar_aula, name='registrar_aula'),
    path('pagina/diario/<int:disciplina_id>/registrarfalta/', views.registrar_falta, name='registrar_falta'),    
    path('pagina/diario/<int:registro_aula_id>/<int:disciplina_id>/registrar-atividade/', views.registrar_atividade, name='registrar_atividade'),    
    
    #cadastro
    path('cadastro/',views.cadastro,name='cadastro'),
    path('cadastro/aluno',views.cadastro_aluno,name='cadastro_aluno'),
    path('cadastro/professor',views.cadastro_professor,name='cadastro_professor'),

    #Boletins aluno
    path('boletin/',views.boletin_aluno,name='boletin'),

    #Popular banco de dados (PRATICIDADE)
    path('popularbd/',views.popular_bd,name='popularBd'),
]