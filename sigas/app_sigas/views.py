from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from .models import Aluno,Professor,Pessoa


'''
CADASTRO - PRECISA ARRUMAR
'''
def cadastro_home(request):
    return render(request,'autenticacao/cadastro/cadastro_home.html')
    
    
def cadastro_aluno(request):
    if request.method == 'POST':
        nome_completo = request.POST.get("nome_completo")
        data_nascimento = request.POST.get("data_nascimento")
        matricula = request.POST.get("matricula")
        curso_superior = request.POST.get("curso_superior")
        senha = request.POST.get("senha")
        email = request.POST.get("email")

        # Criar usuário
        user = User.objects.create_user(username=email, password=senha, email=email, is_active=True)
        user.nome_completo = nome_completo
        user.data_nascimento = data_nascimento
        user.matricula = matricula
        user.save()

        # Criar registro de aluno associado
        aluno = Aluno.objects.create(user=user, curso_superior=curso_superior)
        
        return render(request, 'pagina_sucesso.html')
    else:
        return render(request, 'autenticacao/cadastro/cadastro_aluno.html')
      
        
def cadastro_professor(request):
    if request.method == 'POST':
        nome_completo = request.POST.get("nome_completo")
        data_nascimento = request.POST.get("data_nascimento")
        matricula = request.POST.get("matricula")
        curso_superior = request.POST.get("curso_superior")
        senha = request.POST.get("senha")
        email = request.POST.get("email")

        # Criar usuário
        user = User.objects.create_user(username=email, password=senha, email=email, is_active=True)
        user.nome_completo = nome_completo
        user.data_nascimento = data_nascimento
        user.matricula = matricula
        user.save()

        # Criar registro de aluno associado
        professor = Professor.objects.create(user=user, curso_superior=curso_superior)

        return render(request, 'pagina_sucesso.html')
    else:
        return render(request, 'autenticacao/cadastro/cadastro_professor.html')

    
def logout_view(request):
    logout(request)
    # Redirect to a page after logout
    return redirect('login')



'''
LOGIN - PRECISA REVISAR
'''

def login_view(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Recupere a Pessoa com o nome de usuário fornecido
        # Autentique o usuário com as credenciais fornecidas
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login_django(request, user)
            return redirect('pagina_aluno')  # Redireciona para a página do aluno
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'

    return render(request, 'autenticacao/login/login.html', {'error_message': error_message})




@login_required(login_url='login')
def pagina_aluno(request):
    # Renderize o HTML para a página do aluno
    return render(request, 'users/student/home_student.html')
        


'''
PAGINA DE SUCESS
'''
def pagina_sucesso(request):
    return render(request, 'pagina_sucesso.html')