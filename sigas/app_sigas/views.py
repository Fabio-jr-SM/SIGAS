from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno,Professor
from django.contrib import messages


'''
CADASTRO DE ALUNOS - PRECISA ARRUMAR
'''
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

    
def logout_view(request):
    logout(request)
    # Redirect to a page after logout
    return redirect('login')



'''
LOGIN - PRECISA REVISAR
'''

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if Aluno.objects.filter(id=user.id).exists():
                # Se o usuário for um aluno, redirecione para a página do aluno
                login_required(request, user)
                return redirect('pagina_aluno')
            elif Professor.objects.filter(id=user.id).exists():
                # Se o usuário for um professor, redirecione para a página do professor
                login_required(request, user)
                return redirect('pagina_professor')
            else:
                # Se o usuário não for nem aluno nem professor, redirecione para alguma outra página
                return HttpResponse('Quem é vc zé?')
        else:
            # Usuário ou senha inválidos, redirecione de volta para a página de login com uma mensagem de erro
            return render(request, 'autenticacao/login/login.html', {'error_message': 'Usuário ou senha inválidos.'})
    else:
        # Se o método for GET, exiba a página de login
        return render(request, 'autenticacao/login/login.html')
   

@login_required
def pagina_aluno(request):
    # Renderize o HTML para a página do aluno
    return render(request, 'user/student/home_student.html')

@login_required
def pagina_professor(request):
    # Renderize o HTML para a página do professor
    return render(request, 'user/student/home_student.html')



'''
PAGINA DE SUCESS
'''
def pagina_sucesso(request):
    return render(request, 'pagina_sucesso.html')