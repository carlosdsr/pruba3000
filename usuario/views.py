from django.shortcuts import render, redirect
from .forms import UsuarioForm, ActualizarUsuarioForm
from .models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import ListView
from django.contrib import messages


def registrar(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            try:
                user = form.save()
                user.set_password(user.password)
                messages.success(request, f'Se ha registrado el usuario con exito')
                user.save()
                return redirect('/dashboard-SUP/')
            except:
                pass
    else:
        form = UsuarioForm()
    return render(request, 'usuario/registrarUsuario.html', {'form': form})


class ListaUsuarios(ListView):
    template_name = 'usuario/listaDeUsuarios.html'
    queryset = User.objects.all()


def actualizarUsuario(request):
    if request.method == "POST":
        form = ActualizarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            try:

                user = form.save()
                
                messages.success(request, f'Su perfil se ha actualizado con exito')
                if request.user.cargo:
                    return redirect('/dashboard-SUP/')
                else:
                    return redirect('/dashboard-OPE/')
            except:
                pass
    else:
        form = ActualizarUsuarioForm(instance=request.user)
    if request.user.cargo:
        return render(request, 'usuario/actualizarPerfil.html', {'form': form})
    else:
        return render(request, 'usuario/actualizarPerfil2.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            try:
                form.save()
                update_session_auth_hash(request, form.user)
                if request.user.cargo:
                    return redirect('/dashboard-SUP/')
                else:
                    return redirect('/dashboard-OPE/')
            except:
                pass
    else:
        form = PasswordChangeForm(user=request.user)
    if request.user.cargo:
            return render(request, 'usuario/cambiarpassword.html', {'form': form})
    else:
            return render(request, 'usuario/cambiarpassword2.html', {'form': form})
