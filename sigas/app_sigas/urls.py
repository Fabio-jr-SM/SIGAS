from django.urls import path
from app_sigas import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('', RedirectView.as_view(url='login', permanent=False)), 
    path('logout/', views.logout_view, name='logout'),

    
    path('perfil/',views.perfil,name='perfil'),


    path('pagina/', views.pagina_inicial, name='pagina_inicial'),
    path('pagina/diario', views.diario, name='diario'),
    path('pagina/diario/<int:disciplina_id>/', views.diario_detalhado, name='diario_detalhado'),
    
    path('pagina/diario/registraraula/', views.registrar_aula, name='registrar_aula'),
    path('pagina/diario/registrarfalta/', views.registrar_falta, name='registrar_falta'),
    

    path('popularbd/',views.popular_bd,name='popularBd')
]