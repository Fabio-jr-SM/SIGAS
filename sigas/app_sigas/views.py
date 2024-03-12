from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from .models import Aluno,Pessoa


'''
CADASTRO DE ALUNOS - PRECISA ARRUMAR
'''
def cadastro(request):
    if request.method == 'POST':
        nome_completo = request.POST.get("nome_completo")
        data_nascimento = request.POST.get("data_nascimento")
        matricula = request.POST.get("matricula")
        curso_superior = request.POST.get("curso_superior")
        senha = request.POST.get("senha")
        email = request.POST.get("email")

        # Criar usuário
        user = Pessoa.objects.create_user(username=email, password=senha, email=email, is_active=True)
        user.nome_completo = nome_completo
        user.data_nascimento = data_nascimento
        user.matricula = matricula
        user.save()

        # Criar registro de aluno associado
        aluno = Aluno.objects.create(pessoa=user, curso_superior=curso_superior)

        return render(request, 'pagina_sucesso.html')
    else:
        return render(request, 'autenticacao/cadastro/cadastro.html')

    
def logout_view(request):
    logout(request)
    # Redirect to a page after logout
    return redirect('login')



'''
LOGIN - PRECISA REVISAR
'''

from django.contrib.auth import authenticate, login as login_django
from django.shortcuts import render, redirect
from .models import Pessoa

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Recupere a Pessoa com o nome de usuário fornecido
        pessoa = Pessoa.objects.filter(username=username).first()  # Obtenha a primeira instância de Pessoa com o username fornecido
        print(pessoa.username)
        if pessoa:
            # Autentique o usuário com as credenciais fornecidas
            user = authenticate(request, username=pessoa.username, pessoa.password=password)
            print(user)
            
            if user is not None:
                login_django(request, user)
                print(hasattr(user, 'pessoa'))
                if hasattr(pessoa, 'aluno'):  # Verifica se o usuário é um aluno
                    return redirect('pagina_aluno')  # Redireciona para a página do aluno
                else:
                    return render(request, 'pagina_sucesso.html')  # Redireciona para outra página, se necessário
            else:
                # Autenticação falhou, redirecionar de volta para a página de login com uma mensagem de erro
                return render(request, 'autenticacao/login/login.html', {'error_message': 'Credenciais inválidas. Tente novamente.'})
        else:
            # Caso a Pessoa com o username fornecido não seja encontrada
            return render(request, 'autenticacao/login/login.html', {'error_message': 'Nome de usuário não encontrado.'})

    # Se não for uma solicitação POST, renderize a página de login
    return render(request, 'autenticacao/login/login.html')




@login_required
def pagina_aluno(request):
    # Renderize o HTML para a página do aluno
    return render(request, 'users/student/home_student.html')
        

@login_required
def pagina_aluno(request):
    pass
    # Renderize o HTML para a página do aluno
    #return render(request, 'user/student/home_student.html')


'''
PAGINA DE SUCESS
'''
def pagina_sucesso(request):
    return render(request, 'pagina_sucesso.html')