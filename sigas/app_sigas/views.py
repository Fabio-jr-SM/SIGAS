from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import Aluno,Professor,Pessoa,Curso
import random
import datetime


@login_required(login_url='login')
def perfil(request):
    # Obtém a pessoa associada ao usuário logado
    pessoa_logada = Pessoa.objects.get(user=request.user)
    
    # Obtém o professor associado à pessoa logada
    professor_logado = Professor.objects.get(pessoa=pessoa_logada)
    
    # Prepara os dados do professor para exibição
    dados_professor = {
        'Nome Completo': pessoa_logada.nome_completo,
        'Data de Nascimento': pessoa_logada.data_nascimento,
        'Matrícula': pessoa_logada.matricula,
        'Data de Admissão': professor_logado.data_admissao,
        'Turno': professor_logado.turno,
        'Remuneração': professor_logado.remuneracao
    }
    
    return render(request, 'users/perfil.html', {'dados_professor': dados_professor})

@login_required(login_url='login')
def diario(request):
    professor_logado = Professor.objects.get(pessoa__user=request.user)

    disciplinas_do_professor = professor_logado.disciplina.all()
    
    return render(request,'users/professor/diario.html',{'disciplinas': disciplinas_do_professor})

'''
CADASTRO - PRECISA ARRUMAR
'''

@login_required(login_url='login')
def cadastro_home(request):
    return render(request,'autenticacao/cadastro/cadastro_home.html')
    
    
@login_required(login_url='login')
def cadastro_aluno(request):
    sucess_message = None

    if request.method == 'POST':
        nome_completo = request.POST.get("nome_completo")
        data_nascimento = request.POST.get("data_nascimento")
        matricula = gerar_matricula()
        senha = request.POST.get("senha")
        email = request.POST.get("email")

        # Criar usuário
        user = User.objects.create_user(username=matricula, password=senha, email=email, is_active=True)
        user.nome_completo = nome_completo
        user.data_nascimento = data_nascimento
        user.matricula = matricula
        user.save()

        # Criar registro de aluno associado
        aluno = Aluno.objects.create(user=user, )
        sucess_message = 'Cadastrado com sucesso'
        return render(request, 'autenticacao/cadastro/cadastro_home.html',{'sucess_message': sucess_message})
    else:
        return render(request, 'autenticacao/cadastro/cadastro_aluno.html')
      
        
@login_required(login_url='login')
def cadastro_professor(request):
    pass

    
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
            return redirect('pagina_inicial')  # Redireciona para a página do aluno
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'

    return render(request, 'autenticacao/login/login.html', {'error_message': error_message})




@login_required(login_url='login')
def pagina_inicial(request):
    # Renderize o HTML para a página do aluno
    return render(request, 'users/home_page.html')
        





'''
GERAR MATRICULA
'''
def gerar_matricula():
    # Obter a data atual
    data_atual = datetime.date.today()
    
    # Obter ano, semestre (1 ou 2), dia e um código aleatório de 5 dígitos
    ano = data_atual.year
    semestre = (data_atual.month - 1) // 6 + 1
    dia = data_atual.day
    codigo_aleatorio = random.randint(10000, 99999)
    
    # Formatando a matrícula
    matricula = f"{ano}S{semestre}{dia}{codigo_aleatorio}"
    
    return matricula