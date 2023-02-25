from django.contrib.auth import get_user_model, logout, authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from core.forms import UserAddForm, AddBienForm, DepenseForm
from core.models import Proprietaire, User

Utilisateur = get_user_model()


def add_user(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        type = request.POST.get('type')
        tel = request.POST.get('telephone')
        user_exist = User.objects.filter(email=email)
        if user_exist:
            err = "ERRRRRRR LORS DE LA CREATION DU USER"
            return render(request, 'core/add_user.html', locals())
        else:
            user= User.objects.create_user(
                email=email,
                password=passwd,
                first_name=prenom,
                last_name=nom,
                phoneNumber=tel,
                type=type
            )
            if user:
                if type == 'PROPRIETAIRE':
                    Proprietaire.objects.create(
                        nom=nom,
                        prenom=prenom,
                        email=email,
                        telphone=tel
                    )
                    return redirect('liste_proprietaire')
                elif type == 'GESTIONNAIRE':
                    return redirect('indexGes')
                else:
                    return redirect('index')
            else:
                err = "ERRRRRRR LORS DE LA CREATION DE L'UTILISATEUR :( "
    return render(request, 'core/add_user.html', locals())


def connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        user = authenticate(
            email=email,
            password=passwd
        )
        if user:
            login(request, user)
            if user.type == 'PROPRIETAIRE':
                return redirect('indexPro')
            elif user.type == 'GESTIONNAIRE':
                return redirect('indexGes')
            else:
                return redirect('index')
        else:
            err = 'ERRRRRRRRRRRRR LORS DE L\'AUTHENTIFICATION :('
    return render(request, 'core/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect('connexion')


def is_superuser(user):
    return user.is_superuser


def index(request):
    return render(request, 'core/index.html', locals())


def indexGes(request):
    return render(request, 'core/indexGes.html', locals())


def indexPro(request):
    return render(request, 'core/indexPro.html', locals())


def liste_proprietaire(request):
    return render(request, 'core/liste_proprietaire.html', locals())


def liste_gestionnaire(request):
    return render(request, 'core/liste_gestionnaire.html', locals())


def ajout_bien(request):
    if request.method == 'POST':
        form = AddBienForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('ajou_bien')
    else:
        form = AddBienForm()
    return render(request, 'core/add_bien.html', locals())


def ajout_depense(request):
    form = DepenseForm()
    return render(request, 'core/add_depense.html', locals())


