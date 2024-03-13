from django.contrib import admin
from .models import Pessoa, Aluno, Professor, Curso, Disciplina,RegistroAula,RegistroFalta

# Personalizando a classe de administração para cada modelo

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'data_nascimento', 'matricula', 'user')

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'curso', 'data_de_ingresso', 'situacao_academica')

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'data_admissao', 'turno', 'remuneracao', 'get_disciplinas')

    def get_disciplinas(self, obj):
        return ", ".join([disciplina.nome for disciplina in obj.disciplina.all()])
    get_disciplinas.short_description = 'Disciplinas'

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'duracao')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'turno', 'get_cursos')

    def get_cursos(self, obj):
        return ", ".join([curso.nome for curso in obj.curso.all()])
    get_cursos.short_description = 'Cursos'



class RegistroAulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'horario_inicio','horario_fim','descricao')
class RegistroFaltaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data','aluno','aula')

# Registrando os modelos com suas classes de administração personalizadas

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)

admin.site.register(RegistroAula, RegistroAulaAdmin)
admin.site.register(RegistroFalta, RegistroFaltaAdmin)
