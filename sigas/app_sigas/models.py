import datetime
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.utils.translation import gettext_lazy as _
from django.db import models

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=255, default='')
    data_nascimento = models.DateField(default=datetime.date.today)
    matricula = models.CharField(max_length=20, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', related_name='pessoa')
    
    def __str__(self):
        return self.nome_completo
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='%(app_label)s_%(class)s_groups', # <--- Adicionado
        related_query_name="%(app_label)s_%(class)s",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='%(app_label)s_%(class)s_user_permissions', # <--- Adicionado
        related_query_name="%(app_label)s_%(class)s",
    )  

class Aluno(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    curso = models.ManyToManyField('Curso', related_name='aluno',default='')

    SITUACAO_ACADEMICA_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
        # Adicione mais opções conforme necessário
    ]

    data_de_ingresso = models.DateField(default=datetime.date.today)
    situacao_academica = models.CharField(max_length=20, choices=SITUACAO_ACADEMICA_CHOICES, default='Ativo')
    
    def __str__(self):
        return self.pessoa.nome_completo

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    #disciplina = models.ManyToManyField('Disciplina')
    data_admissao = models.DateField(default=datetime.date.today)
    turno = models.CharField(max_length=100, default='')
    remuneracao = models.FloatField()
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=100,default='')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE,default='')
    
    def __str__(self):
        return self.nome
    
class InscricaoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

class RegistroAula(models.Model):
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    descricao = models.TextField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,default='')
    
    def __str__(self):
        return f"{self.disciplina.nome} - {self.horario_inicio.strftime('%H:%M')}-{self.horario_fim.strftime('%H:%M')}"

class RegistroFalta(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    aula = models.ForeignKey(RegistroAula, on_delete=models.CASCADE,default='')
    quantidade_faltas = models.IntegerField(default=0)
    data = models.DateField(default=datetime.date.today)


#NOVOS
class RegistroAtividade(models.Model):
    descricao = models.TextField()
    registro_aula = models.ForeignKey(RegistroAula, on_delete=models.CASCADE, related_name='atividades')

class notas(models.Model):
    nota = models.FloatField(default='')