from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'rol') and request.user.rol == 'admin':
            return HttpResponse("<h1>Panel de Administración</h1>")
        else:
            return render(request, 'usuarios/home.html')
    else:
        return redirect('login')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")  
        else:
            return render(request, "usuarios/login.html", {"error": "Credenciales incorrectas"})
    return render(request, "usuarios/login.html")

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
