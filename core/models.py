from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    TYPE = (
        ('GESTIONNAIRE', 'GESTIONNAIRE'),
        ('PROPRIETAIRE', 'PROPRIETAIRE'),
    )
    type = models.CharField(max_length=255, choices=TYPE)
    phoneNumber = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Proprietaire(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telphone = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default='PROPRIETAIRE')

    def __str__(self):
        return self.nom


class Biens(models.Model):
    loyer = models.FloatField(default=0.0)
    quartier = models.CharField(max_length=255)
    nbrePiece = models.IntegerField(default=1)
    nbreChambre = models.IntegerField(default=1)
    gestionnaire = models.ForeignKey(User, on_delete=models.CASCADE)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)


class Locataire(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    bien = models.OneToOneField(Biens, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Depense(models.Model):
    nomDepense = models.CharField(max_length=255)
    description = models.TextField()
    fraisDepense = models.FloatField(default=0.0)
    bien = models.ForeignKey(Biens, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomDepense
