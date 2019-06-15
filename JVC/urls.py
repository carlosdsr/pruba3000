from django.contrib import admin
from django.urls import path, include
from usuario import views as Usuario_views
from django.contrib.auth.decorators import login_required
from centralesElectricas import views as centralesViews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cambiarpassword/', login_required(Usuario_views.change_password), name='cambiar_password'),
    path('registroUsuario/', login_required(Usuario_views.registrar), name='registroUsuario'),
    path('gestionUsuario/', login_required(Usuario_views.ListaUsuarios.as_view()), name='gestionUsuario'),
    path('registrarNodo/', login_required(centralesViews.registrarNodo), name='registrarNodo'),
    path('Perfil/', login_required(Usuario_views.actualizarUsuario), name='perfil'),
    path('editarNodos/', login_required(centralesViews.editarNodos), name='editarNodo'),
    path('eliminarNodos/', login_required(centralesViews.eliminarNodos), name='eliminarNodo'),
    path('asociarNodos/', login_required(centralesViews.asociarNodos), name='asociarNodos'),
    path('listaDeCentrales/', login_required(centralesViews.ListaDeCentrales.as_view()), name='listaDeCentrales'),
    path('', include('home.urls')),
]
