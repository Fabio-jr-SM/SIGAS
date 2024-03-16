from django.contrib import admin
from .models import InscricaoDisciplina, Pessoa, Aluno, Professor, Curso, Disciplina,RegistroAula,RegistroFalta

# Personalizando a classe de administração para cada modelo

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'data_nascimento', 'matricula', 'user')

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'get_cursos', 'data_de_ingresso', 'situacao_academica')

    def get_cursos(self, obj):
        return ", ".join([curso.nome for curso in obj.curso.all()])

    get_cursos.short_description = 'Cursos'


class InscricaoDisciplinaInline(admin.TabularInline):
    model = InscricaoDisciplina
    extra = 1

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'data_admissao', 'turno', 'remuneracao', 'get_disciplinas')

    def get_disciplinas(self, obj):
        return ", ".join([inscricao.disciplina.nome for inscricao in obj.inscricaodisciplina_set.all()])
    
    get_disciplinas.short_description = 'Disciplinas'

    inlines = [InscricaoDisciplinaInline]


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'duracao')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'turno', 'curso')

    



class RegistroAulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'horario_inicio','horario_fim','descricao')

class RegistroFaltaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data','aluno','aula','quantidade_faltas')

# Registrando os modelos com suas classes de administração personalizadas

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)

admin.site.register(RegistroAula, RegistroAulaAdmin)
admin.site.register(RegistroFalta, RegistroFaltaAdmin)
