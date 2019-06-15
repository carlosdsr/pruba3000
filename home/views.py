from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings


def home(request):
    return render(request, 'home/inicioSesion.html')


def dashboard(request):
    return render(request, 'home/dashboard-OPE.html')


def dashboard2(request):
    return render(request, 'home/dashboard-SUP.html')


def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.cargo:
                return redirect('dashboardjvc2')
            else:        
                return redirect('dashboardjvc')
    else:
        form = AuthenticationForm()
    return render(request, 'home/inicioSesion.html', {'form': form})


def logoutview(request):
    if request.method == 'POST':
        logout(request)
        form = AuthenticationForm()
        return redirect(settings.LOGIN_URL)
