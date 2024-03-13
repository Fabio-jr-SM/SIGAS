from django.urls import path
from app_sigas import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('perfil/',views.perfil,name='perfil'),
    path('', RedirectView.as_view(url='login', permanent=False)), 

    
    path('logout/', views.logout_view, name='logout'),
    path('pagina/', views.pagina_inicial, name='pagina_inicial'),


    path('pagina/diario', views.diario, name='diario'),

    path('popularbd/',views.popular_bd,name='popularBd')
]