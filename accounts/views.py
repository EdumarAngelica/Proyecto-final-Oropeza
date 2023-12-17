from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            data = form.cleaned_data
            usuario = data.get('username')
            contrasenia = data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user:
                login(request, user) #NO TENGO CLARO A DONDE REDIRECCIONAR SERÁ ¿PRODUCTLIST?

        return redirect('ProductList')

    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)

def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    

    form= UserRegisterForm()
    contexto= {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)

@login_required
def editar_request(request):
    user = request.user
    if request.method == "POST":

        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.email = request.POST["email"]
            user.save()
            return redirect("ProductList")
    
    form= UserUpdateForm(initial= {"username": user.username, "email": user.email})
    contexto= {
    "form": form
} 
    return render(request, "accounts/registro.html", contexto)  

@login_required
def editar_avatar_request(request):
    user = request.user

    form = AvatarUpdateForm()
    contexto= {
    "form": form
} 
    return render(request, "accounts/registro.html", contexto)  