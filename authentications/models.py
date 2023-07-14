from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
       def create_user(self, email, password=None, **extra_fields):
           if not email:
               raise ValueError("The Email field must be set")
           
           email = self.normalize_email(email)
           user = self.model(email=email, **extra_fields)
           user.set_password(password)
           user.save(using=self._db)
           return user
       
       def create_superuser(self, email, password=None, **extra_fields):
           extra_fields.setdefault('is_staff', True)
           extra_fields.setdefault('is_superuser', True)
           
           return self.create_user(email, password, **extra_fields)
       
       
class CustomUser(AbstractBaseUser, PermissionsMixin):
             GENDER = [
                ('Male','Male'),
                ('Female','Female'),
                ('Other','Other')
             ]
            
             email = models.EmailField(unique=True)
             first_name = models.CharField(max_length=250,null=True)
             last_name  = models.CharField(max_length=200,null=True)
             date_of_birth = models.DateField(default=timezone.now,null=True)
             gender = models.CharField(max_length=40,choices=GENDER,null=True)
             role  = models.IntegerField(null=True)
             image = models.FileField(upload_to='user')
             
             objects = CustomUserManager()

             USERNAME_FIELD = 'email'
             
