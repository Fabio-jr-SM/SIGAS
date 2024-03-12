# Generated by Django 4.2.9 on 2024-03-12 14:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_sigas', '0004_alter_aluno_options_alter_pessoa_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='curso_superior',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='disciplinas',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='professor',
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='aluno', to='app_sigas.curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='data_de_ingresso',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='aluno',
            name='situacao_academica',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', max_length=20),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='curso',
            field=models.ManyToManyField(default='', related_name='disciplinas', to='app_sigas.curso'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='turno',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='professor',
            name='disciplina',
            field=models.ManyToManyField(to='app_sigas.disciplina'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='pessoa', to=settings.AUTH_USER_MODEL),
        ),
    ]