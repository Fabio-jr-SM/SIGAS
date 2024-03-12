from django.urls import path
from app_sigas import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('perfil/',views.perfil,name='perfil'),
    path('', RedirectView.as_view(url='login', permanent=False)), 

    path('cadastro/',views.cadastro_home,name='cadastro'),
    path('cadastro/aluno',views.cadastro_aluno,name='cadastro_aluno'),
    path('cadastro/professor',views.cadastro_professor,name='cadastro_professor'),
    
    path('logout/', views.logout_view, name='logout'),
    path('pagina/', views.pagina_inicial, name='pagina_inicial'),


    path('pagina/diario', views.diario, name='diario'),

    #path('pagina/professor', views.pagina_professor, name='pagina_professor'),
]