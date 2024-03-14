from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import Aluno,Professor,Pessoa,Curso,Disciplina,RegistroAula, RegistroFalta
import random
import datetime
from django.http import HttpResponseBadRequest
from django.shortcuts import reverse

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


def diario_detalhado(request, disciplina_id):
    # Obtenha a disciplina com o ID fornecido ou retorne um erro 404 se não existir
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)

    # Acesse os registros de aula relacionados à disciplina específica
    registros_aula = RegistroAula.objects.filter(disciplina=disciplina)

    # Construa a URL reversa para a view registrar_aula com o argumento disciplina_id
    #url_registrar_aula = reverse('registrar_aula', kwargs={'disciplina_id': disciplina_id})

    return render(request, 'users/professor/diario_detalhado.html', {'disciplina': disciplina, 'registros_aula': registros_aula, 'disciplina_id': disciplina_id})

@login_required(login_url='login')
def registrar_aula(request, disciplina_id):
    if request.method == 'POST':
        horario_inicio = request.POST.get('horario_inicio')
        horario_fim = request.POST.get('horario_fim')
        descricao = request.POST.get('descricao')

        

        disciplina = get_object_or_404(Disciplina, id=disciplina_id)

        # Crie um novo registro de aula
        registro_aula = RegistroAula.objects.create(
            horario_inicio=horario_inicio,
            horario_fim=horario_fim,
            descricao=descricao,
            disciplina=disciplina
        )

        # Redirecione para a página de detalhes do diário com o ID do registro de aula
        return redirect('diario_detalhado', disciplina_id=disciplina_id)

    return render(request, 'users/professor/registrar_aula.html', {'disciplina_id': disciplina_id})

def registrar_falta(request):
    disciplina_id = 1
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    alunos = Aluno.objects.filter(curso=disciplina.curso)
    faltas = RegistroFalta.objects.filter(aula__disciplina=disciplina)

    if request.method == 'POST':
        pass

    return render(request, 'registrar_falta.html', {'disciplina': disciplina, 'alunos': alunos, 'faltas': faltas})

    

    '''if request.method == 'POST':
        aluno_id = request.POST.get('aluno_id')
        aula_id = request.POST.get('aula_id')
        quantidade_faltas = request.POST.get('quantidade_faltas')

        # Crie um novo registro de falta
        registro_falta = RegistroFalta.objects.create(
            aluno_id=aluno_id,
            aula_id=aula_id,
            quantidade_faltas=quantidade_faltas
        )

        # Redirecione para onde você deseja após o registro de falta
        return redirect('diario_detalhado')

    return render(request, 'users/professor/registrar_falta.html')'''

    
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



'''
POPULANDO O BANCO DE DADOS
'''
def popular_bd(request):

    # Criando superusuário
    User.objects.create_superuser('admin', 'admin@example.com', '1234')

    # Criando usuários
    professor_user = User.objects.create_user(username='professor', password='senha123')
    aluno_user = User.objects.create_user(username='aluno', password='senha123')

    # Criando pessoas
    professor_pessoa = Pessoa.objects.create(nome_completo='Nome do Professor', 
                                              data_nascimento=datetime.date(1980, 1, 1), 
                                              matricula='0001',
                                              user=professor_user)
    aluno_pessoa = Pessoa.objects.create(nome_completo='Nome do Aluno', 
                                          data_nascimento=datetime.date(1990, 1, 1), 
                                          matricula='0002',
                                          user=aluno_user)

    # Criando cursos
    curso1 = Curso.objects.create(nome='Engenharia da Computação', duracao='4 anos')
    curso2 = Curso.objects.create(nome='Engenharia Aeronautica', duracao='3 anos')

    # Criando disciplinas
    disciplina1 = Disciplina.objects.create(nome='Algoritmos', turno='Manhã')
    disciplina2 = Disciplina.objects.create(nome='Metodologia Cientifica', turno='Tarde')
    disciplina3 = Disciplina.objects.create(nome='Algebra Linear', turno='Noite')

    # Relacionando disciplinas com cursos
    disciplina1.curso.add(curso1)
    disciplina2.curso.add(curso1, curso2)
    disciplina3.curso.add(curso2)

    # Criando professores e associando disciplinas
    professor = Professor.objects.create(pessoa=professor_pessoa,
                                         data_admissao=datetime.date(2020, 1, 1),
                                         turno='Integral',
                                         remuneracao=5000.00)
    professor.disciplina.add(disciplina1, disciplina2)

    # Criando aluno e associando curso
    aluno = Aluno.objects.create(pessoa=aluno_pessoa,
                                 curso=curso1,
                                 data_de_ingresso=datetime.date(2022, 1, 1),
                                 situacao_academica='Ativo')

    sucess_message = "Banco de dados populado com sucesso!"
    return render(request, 'autenticacao/login/login.html', {'sucess_message': sucess_message})
