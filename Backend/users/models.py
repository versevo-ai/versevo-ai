from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# class newUserManager(UserManager):
#     def create_user(self, username, email, password, **extra_fields):
#         """
#         Creates a new regular user.
#         """
        
#         username = "".join(str(username).split(" "))
#         email = "".join(str(email).split(" "))
#         password = "".join(str(password).split(" "))


#         if not username:
#             raise ValidationError("Users must have a username")
#         if not email:
#             raise ValidationError("Users must have an email address")
#         if not password:
#             raise ValidationError("Users must have a password")

#         user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password, **extra_fields):
#         """
#         Creates a new superuser.
#         """
        
#         if not username:
#             raise ValidationError("Superusers must have a username")
#         if not email:
#             raise ValidationError("Superusers must have an email address")
#         if not password:
#             raise ValidationError("superusers must have a password")
        
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         return self.create_user(username, email, password, **extra_fields)

class NewUser(AbstractUser):
    """
    This model is used to redefine the user model with additional fields like 'Bearer_Token' , 'Refresh_Token' , 'Blacklisted'.
    It is an independent Model , having
    """
    
    username = models.CharField(primary_key=True,max_length=150)
    Bearer_Token = models.CharField()
    Refresh_Token = models.CharField()
    Blacklisted = models.BooleanField(default=False)
    
    USERNAME_FIELD = username
    
    REQUIRED_FIELDS = ['username','Bearer_Token', 'Refresh_Token', 'Blacklisted']  # Include required fields

    # objects = newUserManager()

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
