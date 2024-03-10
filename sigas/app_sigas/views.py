from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'GET':
        return render(request,'autenticacao/cadastro/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Usuario já cadastrado')
        
        user = User.objects.create_user(username=username,email=email,password=senha)
        user.save()
        
        return HttpResponse("Usuario cadastrado com sucesso")
    
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