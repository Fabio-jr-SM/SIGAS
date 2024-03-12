from django.urls import path
from app_sigas import views
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('pagina/aluno', views.pagina_aluno, name='pagina_aluno'),
    #path('pagina/professor', views.pagina_professor, name='pagina_professor'),
]