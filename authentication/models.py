from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    #override create_user and create_superuser
    def create_user(self,email,password,**extra_fields):
      if not email:
         raise ValueError(_("Email must be provided"))
      email = self.normalize_email(email) #turn the email into lowercase
      new_user = self.model(email=email,**extra_fields)

      new_user.set_password(password) # set_password() gets the new user & then hashes and store them in the database
      new_user.save()

      return new_user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', False) 

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as true"))
        
        if extra_fields.get('is_superuser') is not True:
           raise ValueError(_("Superuser should have is_superuser as TRUE"))
        
        if extra_fields.get('is_active') is not True:
           raise ValueError(_("Superuser should have is_active as TRUE"))
        
        return self.create_user(email,password,**extra_fields)
    
#after doing the validation we are going to create our custom user model
class User(AbstractUser):
   username = models.CharField(max_length=25, unique=True)
   email = models.EmailField(max_length=80, unique=True)
   phone_number = PhoneNumberField(null=False, unique=True)
   #since we are building on top of User model we aren't required to have an extra password field since it going tobe
   #part of our User model

   #user email field as user name
   USERNAME_FIELD='email'

   #define required fields
   REQUIRED_FIELDS=['username', 'phone_number']
    
   #specify how user objects are going to be created
   objects = CustomUserManager()

   #return strig representation of every user object we create
   def __str__(self):
      return f"<User {self.email}"