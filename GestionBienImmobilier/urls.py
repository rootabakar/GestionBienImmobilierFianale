"""GestionBienImmobilier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexGes/', indexGes, name='indexGes'),
    path('', index, name='index'),
    path('indexPro/', indexPro, name='indexPro'),
    path('add-user/', add_user, name='addUser'),
    path('connexion/', connexion, name='connexion'),
    path('liste-proprietaire/', liste_proprietaire, name='liste_proprietaire'),
    path('liste-gestionnaire/', liste_gestionnaire, name='liste_gestionnaire'),
    path('deconnexion/', deconnexion, name='deconnexion'),
]
