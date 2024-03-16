from django.shortcuts import render,redirect,get_object_or_404 

#autenticacao
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#banco de dados
from .models import Aluno, InscricaoDisciplina,Professor,Pessoa,Curso,Disciplina,RegistroAula, RegistroFalta

#calendario
import calendar
from datetime import datetime as data_atual

#gerar matricula
import random
import datetime

#Envio de Email
from django.core.mail import send_mail

#permissoes
from .roles import Alunopermission, Professorpermission
from rolepermissions.roles import assign_role


@login_required(login_url='login')
def pagina_inicial(request):

    now = data_atual.now()
    ano_atual = now.year
    mes_atual = now.month

    # Crie um calendário para o mês atual
    cal = calendar.monthcalendar(ano_atual, mes_atual)

    if hasattr(request.user, 'pessoa'):
        pessoa_logada = request.user.pessoa
        return render(request, 'users/home_page.html', {'pessoa_logada': pessoa_logada,'cal': cal})
    elif request.user.is_superuser:
        return render(request, 'users/home_page.html',{'cal': cal})


'''
PERFIL GERAL - PROFESSOR, ALUNO E ADMINISTRADOR
'''
@login_required(login_url='login')
def perfil(request):
    # Obtém a pessoa associada ao usuário logado
    pessoa_logada = get_object_or_404(Pessoa, user=request.user)
    
    return render(request, 'users/perfil.html', {'pessoa_logada': pessoa_logada})

'''
DIARIOS DO PROFESSOR
'''
@login_required(login_url='login')
def diario(request):
    pessoa_logada = get_object_or_404(Pessoa, user=request.user)

    professor_logado = Professor.objects.get(pessoa__user=request.user)

    disciplinas_do_professor = InscricaoDisciplina.objects.filter(professor=professor_logado)

    return render(request, 'users/professor/diario.html', {'disciplinas': disciplinas_do_professor,'pessoa_logada':pessoa_logada})

@login_required(login_url='login')
def diario_detalhado(request, disciplina_id):
    pessoa_logada = get_object_or_404(Pessoa, user=request.user)

    # Obtenha a disciplina com o ID fornecido ou retorne um erro 404 se não existir
    disciplina = get_object_or_404(InscricaoDisciplina, disciplina_id=disciplina_id)

    # Acesse os registros de aula relacionados à disciplina específica
    registros_aula = RegistroAula.objects.filter(disciplina=disciplina.disciplina)

    return render(request, 'users/professor/diario_detalhado.html', 
                  {'disciplina': disciplina.disciplina, 
                   'registros_aula': registros_aula, 
                   'disciplina_id': disciplina_id,
                   'pessoa_logada':pessoa_logada})


'''
REGISTRO DE AULA E FALTA
'''
#Falta registro de atividade
@login_required(login_url='login')
def registrar_aula(request, disciplina_id):
    pessoa_logada = get_object_or_404(Pessoa, user=request.user)
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

    return render(request, 'users/professor/registrar_aula.html', {'disciplina_id': disciplina_id,
                                                                   'pessoa_logada':pessoa_logada})


@login_required(login_url='login')
def registrar_falta(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    pessoa_logada = get_object_or_404(Pessoa, user=request.user)
    # Acessando os alunos diretamente através do relacionamento com a disciplina
    alunos = Aluno.objects.filter(curso=disciplina.curso)
    
    if request.method == "POST":
        for aluno in alunos:
            quantidade_faltas = request.POST.get(f"quantidade_faltas_{aluno.id}")
            aula_id = RegistroAula.objects.filter(disciplina=disciplina).first()

            # Busque o objeto Aluno com base no ID fornecido
            aluno = Aluno.objects.get(pk=aluno.id)

            # Verifique se a aula_id não é None antes de criar o RegistroFalta
            if aula_id is not None:
                RegistroFalta.objects.create(aluno=aluno, aula=aula_id, quantidade_faltas=quantidade_faltas)
                return redirect('diario')
            else:
                return render(request, 'users/professor/registrar_falta.html', {'disciplina': disciplina, 'disciplina_id': disciplina_id, 'alunos': alunos})

    return render(request, 'users/professor/registrar_falta.html', {'disciplina': disciplina, 
                                                                    'disciplina_id': disciplina_id, 
                                                                    'alunos': alunos,
                                                                    'pessoa_logada':pessoa_logada})



'''
LOGIN E LOGOUT
'''
    
def logout_view(request):
    logout(request)
    # Redirect to a page after logout
    return redirect('login')


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
    disciplina1 = Disciplina.objects.create(nome='Algoritmos', turno='Manhã',curso=curso1)
    disciplina2 = Disciplina.objects.create(nome='Metodologia Cientifica', turno='Tarde',curso=curso1)
    disciplina3 = Disciplina.objects.create(nome='Algebra Linear', turno='Noite',curso=curso2)

    # Criando professores e associando disciplinas
    professor = Professor.objects.create(pessoa=professor_pessoa,
                                         data_admissao=datetime.date(2020, 1, 1),
                                         turno='Integral',
                                         remuneracao=5000.00)
    inscricao = InscricaoDisciplina.objects.create(professor=professor,disciplina=disciplina1)
    inscricao = InscricaoDisciplina.objects.create(professor=professor,disciplina=disciplina2)

    # Criando aluno e associando curso
    aluno = Aluno.objects.create(pessoa=aluno_pessoa,
                                 data_de_ingresso=datetime.date(2022, 1, 1),
                                 situacao_academica='Ativo')
    aluno.curso.add(curso1)  # Adicionando o curso ao aluno

    success_message = "Banco de dados populado com sucesso!"
    return render(request, 'autenticacao/login/login.html', {'success_message': success_message})



'''
CADASTRO DE PROFESSOR E ALUNO
'''
def cadastro(request):
    alunos = Aluno.objects.all()
    professores = Professor.objects.all()
    
    return render(request,'autenticacao/cadastro/cadastro_home.html',{'alunos': alunos, 'professores': professores})

def cadastro_aluno(request):
    cursos = Curso.objects.all()

    if request.method == "POST":
        username_matricula = gerar_matricula()
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        nome_completo = request.POST.get("nome_completo")
        data_nasc = request.POST.get("data_nasc")
        curso_escolhido_id = request.POST.get("curso")
        curso = Curso.objects.get(pk=curso_escolhido_id)

        #criando usuario
        aluno_user = User.objects.create_user(username=username_matricula, password=senha,email=email)
        
        aluno_user.save()
        #dando acesso somente a pagina do professor
        assign_role(aluno_user,Alunopermission)

        #criando pessoa
        aluno_pessoa = Pessoa.objects.create(nome_completo=nome_completo, 
                                          data_nascimento=data_nasc, 
                                          matricula=username_matricula,
                                          user=aluno_user)
        
        aluno = Aluno.objects.create(pessoa=aluno_pessoa,
                                 data_de_ingresso=datetime.date.today(),
                                 situacao_academica='Ativo')
        
        aluno.curso.add(curso)  # Adicionando o curso ao aluno

        #enviando email de Confirmação de Inscrição
        send_mail('SIGAS - Confirmação de Matrícula',
                  f'Bem vindo aluno, {nome_completo} a plataforma SIGAS!\nSua matrícula: {username_matricula}\nSua Senha: {senha}',
                  'sistema.sigas@gmail.com',
                  [email])

        return redirect('cadastro')
    return render(request,'autenticacao/cadastro/cadastro_aluno.html',{'cursos':cursos})

def cadastro_professor(request):
    cursos = Curso.objects.all()

    # Lista para armazenar pares de (disciplina, curso)
    disciplinas_com_cursos = []

    # Para cada curso, obtém todas as disciplinas associadas
    for curso in cursos:
        disciplinas = curso.disciplina_set.all()  # Obtém todas as disciplinas associadas ao curso
        for disciplina in disciplinas:
            # Adiciona a disciplina juntamente com o curso à lista
            disciplinas_com_cursos.append((disciplina, curso))
    
    if request.method == 'POST':
        username_matricula = gerar_matricula()
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        nome_completo = request.POST.get("nome_completo")
        data_nasc = request.POST.get("data_nasc")
        matricula_professor = gerar_matricula()
        turno = request.POST.get("turno")
        remuneracao = request.POST.get("remuneracao")

        #criando usuario professor
        professor_user = User.objects.create_user(username=matricula_professor, password=senha,email=email)
        
        professor_user.save()
        #dando acesso somente a pagina do professor
        assign_role(professor_user,Professorpermission)
        #criando pessoa professor
        professor_pessoa = Pessoa.objects.create(nome_completo=nome_completo, 
                                              data_nascimento=data_nasc, 
                                              matricula=matricula_professor,
                                              user=professor_user)
        
        # Criando professores e associando disciplinas
        professor = Professor.objects.create(pessoa=professor_pessoa,
                                            data_admissao=datetime.date.today(),
                                            turno=turno,
                                            remuneracao=remuneracao)
        
        # Adicionar disciplinas selecionadas ao professor
        disciplinas_selecionadas = request.POST.getlist('disciplinas')
        for disciplina_id in disciplinas_selecionadas:
            disciplina = Disciplina.objects.get(pk=disciplina_id)
            inscricao = InscricaoDisciplina.objects.create(professor=professor,disciplina=disciplina)
        
        send_mail('SIGAS - Confirmação de Matrícula',
                  f'Bem vindo professor, {nome_completo} a plataforma SIGAS!\nSua matrícula: {username_matricula}\nSua Senha: {senha}',
                  'sistema.sigas@gmail.com',
                  [email])

        return redirect('cadastro')
    
    return render(request,'autenticacao/cadastro/cadastro_professor.html',{'disciplinas_com_cursos': disciplinas_com_cursos})

