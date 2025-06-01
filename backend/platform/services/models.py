from django.db import models
from engine.settings import AUTH_USER_MODEL
from versemodels.models import ChatModels

# Create your models here.

# User's profile page will be using 2 db models - NewUser + Services

class services(models.Model):       # This model will populate data at /USER-PROFILE/SERVICE page
   
    # Whenever user will go to /EXPLORE/ page , data from Chatmodels of VERSEMODELS will be populated
    # User has to click on a particular one , which will redirect to a new page having model-name as query parameter
    # From there user can see the details and whenever user purchases ,
    # The corresponding service model record will be updated
    
    
    username = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="NewUser")
    Mname = models.ForeignKey(ChatModels,on_delete=models.SET_NULL,related_name="ChatModels")
    Mcategory = models.TextField()
    Mparams = models.CharField()
    Mtags = models.CharField()
    Mdescription = models.CharField()
    Mprice = models.DecimalField(null=True, blank=True, default=0.00,decimal_places=2)

    def __str__(self):
        return f"{self.user} spent {self.money}"