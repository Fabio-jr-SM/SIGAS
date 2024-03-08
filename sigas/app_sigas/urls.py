from django.urls import path
from app_sigas import views
urlpatterns = [
    path('cadastro/',views.cadastro,name='cadastro'),
    path('login/',views.login,name='login')
]