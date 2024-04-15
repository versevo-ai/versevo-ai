from django.db import models
from engine.settings import AUTH_USER_MODEL

# Create your models here.

class services(models.Model):
    user = models.ManyToManyField(AUTH_USER_MODEL, related_name="users" ,null=True, blank = True, on_delete=models.CASCADE)
    username = models.CharField(null=True, blank = True,default="NULL")
    money = models.FloatField(null=True, blank = True,default=0)
    text_to_speech = models.BooleanField(null=True, blank = True,default=False)
    speech_to_text = models.BooleanField(null=True, blank = True,default=False)
    speech_to_speech = models.BooleanField(null=True, blank = True,default=False)
    
    def __str__(self):
        return f"{self.username} - TTS : {self.text_to_speech} , STT : {self.speech_to_text} , STS : {self.speech_to_speech}"
    
    
     
    
