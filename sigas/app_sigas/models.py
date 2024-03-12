import datetime
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.utils.translation import gettext_lazy as _
from django.db import models

class Pessoa(AbstractUser):
    nome_completo = models.CharField(max_length=255,default='')
    data_nascimento = models.DateField(default=datetime.date.today)
    matricula = models.CharField(max_length=20,default='')
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    # Especificando related_name para evitar conflito
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
    curso_superior = models.CharField(max_length=100,default='')

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"