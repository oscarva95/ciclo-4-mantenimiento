from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db.models.fields import EmailField
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    rol = models.CharField('Rol',max_length=15,default='consultor')
    username = models.CharField('Username',max_length=15,unique=True)
    password = models.CharField('Password',max_length=256)
    name = models.CharField('Name', max_length=30)
    email = models.EmailField('Email',max_length=150,null=True)

    #para encriptar contraseñas
    def save(self, **kwargs):
        some_salt='mMuj0DrIK6vgtdIYepKIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    USERNAME_FIELD ='username'
    objects = UserManager()