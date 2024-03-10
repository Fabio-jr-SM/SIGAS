from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Aluno.objects.create(pessoa=user, numero_matricula=form.cleaned_data['numero_matricula'])
            return redirect('pagina_sucesso')
    else:
        form = UserCreationForm()
    return render(request, 'autenticacao/cadastro/cadastro.html', {'form': form})

def pagina_sucesso(request):
    return render(request, 'pagina_sucesso.html')
    
def logout_view(request):
    logout(request)
    # Redirect to a page after logout
    return redirect('login')


def login(request):
    if request.method == "GET":
        return render(request,'autenticacao/login/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')
        
        user = authenticate(username=username,password=senha)

        if user:
            login_django(request,user)

            return render(request,'users/student/home_student.html')
        else:
            return HttpResponse('Não autenticado')


@login_required(login_url="login")    
def plataforma(request):
    return render(request,'users/student/home_student.html')