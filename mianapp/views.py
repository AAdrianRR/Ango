from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Vista principal (Inicio)
def index(request):
    return render(request, "mainapp/index.html", {
        'title': 'Inicio',
        'content': 'Bienvenido al inicio'
    })

# Vista "Acerca de"
def about(request):
    return render(request, "mainapp/about.html", {
        'title': 'Acerca de',
        'content': 'Soy Acerca de'
    })

# Vista "Misión"
def mision(request):
    return render(request, "mainapp/mision.html", {
        'title': 'Misión',
        'content': 'Soy Misión'
    })

# Vista "Visión"
def vision(request):
    return render(request, "mainapp/vision.html", {
        'title': 'Visión',
        'content': 'Soy Visión'
    })

# Manejo de errores 404
def redirigir_inicio(request, exception):
    return render(request, 'mainapp/404.html', {
        'title': 'Página no encontrada'
    })

def registro(request):  
    if request.user.is_authenticated:
        return redirect('inicio')  
    else:
        register_form = UserCreationForm()  

        if request.method == "POST":
            register_form = UserCreationForm(request.POST)

            if register_form.is_valid():
                register_form.save()  
                messages.success(request, "¡Registro con éxito!")  
                return redirect('sesion')  

        return render(request, 'mainapp/registro.html', { 
            'title': 'Registro de Usuario',
            'register_form': register_form,
        })


    return render(request, 'mainapp/registro.html', {
        'title': 'Registro',
        'form': form,
    })

# Inicio de sesión
def sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirigir al inicio si las credenciales son válidas
        else:
            return render(request, 'mainapp/sesion.html', {
                'title': 'Inicio de sesión',
                'error': 'Credenciales inválidas',
            })
    return render(request, 'mainapp/sesion.html', {
        'title': 'Inicio de sesión',
    })

def logout_user(request):
    logout(request)
    return redirect('sesion')


