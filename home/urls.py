from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.loginview, name='iniciojvc'),
    path('logout/', login_required(views.logoutview), name='cerrarjvc'),
    path('dashboard-OPE/', login_required(views.dashboard), name='dashboardjvc'),
    path('dashboard-SUP/', login_required(views.dashboard2), name='dashboardjvc2'),
]
