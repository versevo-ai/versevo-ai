from django.db import models
from engine.settings import AUTH_USER_MODEL

# Create your models here.


class services(models.Model):
    username = models.CharField(null=True, blank=True, default="NULL")
    money = models.FloatField(null=True, blank=True, default=0)
    text_to_speech = models.BooleanField(null=True, blank=True, default=False)
    speech_to_text = models.BooleanField(null=True, blank=True, default=False)
    speech_to_speech = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return f"{self.username} - TTS : {self.text_to_speech} , STT : {self.speech_to_text} , STS : {self.speech_to_speech}"


class UserService(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(services, on_delete=models.CASCADE)
