from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,firstname,lastname,email,username,mobile,password=None):
        if not username:
            raise ValueError('User must have an Username')
        if not email:
            raise ValueError('User Must Have an email ID')
        if not mobile:
            raise ValueError('User Must have a Mobile Number')
        user=self.model(
        firstname=firstname,
        lastname=lastname,
        email=self.normalize_email(email),
        username=username,
        mobile=mobile,
        )


        user.set_password(password)
        user.save(using=self._db)
        return  user

    def create_superuser(self,firstname,lastname,email,username,mobile,password):
        user=self.create_user(
        firstname=firstname,
        lastname=lastname,
        email=email,
        username=username,
        mobile=mobile,
        password=password,

        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_admin=True
        user.is_superadmin=True

        user.save(using=self._db)
        return user
class Account(AbstractBaseUser):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    mobile=models.CharField(max_length=12)
    #required
    is_active=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    last_login=models.DateField(auto_now_add=True)
    date_joined=models.DateField(auto_now_add=True)
    objects=MyAccountManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstname','lastname','username','mobile']
    def __str__(self):
        return self.email
    def fullname(self):
        return f'{self.firstname}{self.lastname}'
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,add_label):
        return True
