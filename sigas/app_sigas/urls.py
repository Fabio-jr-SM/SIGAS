from django.urls import path
from app_sigas import views
urlpatterns = [
    path('',views.login,name='login'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('plataforma/',views.plataforma,name='plataforma'),
    path('logout/', views.logout_view, name='logout'),
]