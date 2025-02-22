from django.db import models
from engine.settings import AUTH_USER_MODEL

# Create your models here.


class services(models.Model):
    TTS_MODEL_NAMES= {
        'TTS_Model1':'tts_model1',
        'TTS_Model2':'tts_model2',
        'TTS_Model3':'tts_model3',
    }
    
    TTS_MODEL_PRICES= {
        'tts_model1':100,
        'tts_model2':200,
        'tts_model3':300,
    }
    
    
    
    STT_MODEL_NAMES= {
        'STT_Model1':'stt_model1',
        'STT_Model2':'stt_model2',
        'STT_Model3':'stt_model3',
    }
    
    STT_MODEL_PRICES= {
        'stt_model1':100,
        'stt_model2':200,
        'stt_model3':300,
    }
    
    
    STS_MODEL_NAMES= {
        'STS_Model1':'sts_model1',
        'STS_Model2':'sts_model2',
        'STS_Model3':'sts_model3',
    }
    
    STS_MODEL_PRICES= {
        'sts_model1':100,
        'sts_model2':200,
        'sts_model3':300,
    }
    
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="NewUser")
    money = models.IntegerField(null=True, blank=True, default=0)
    tts_model = models.TextField(choices=TTS_MODEL_NAMES)
    
    stt_model = models.TextField(choices=STT_MODEL_NAMES)
    
    sts_model = models.TextField(choices=STS_MODEL_NAMES)
    
    def save(self, *args, **kwargs):
        
        price = self.TTS_MODEL_PRICES.get(self.TTS_MODEL_NAMES.get(self.tts_model))
        print(price)
        self.money += price
        
        price = self.STT_MODEL_PRICES.get(self.STT_MODEL_NAMES.get(self.stt_model))
        self.money += price
        
        price = self.STS_MODEL_PRICES.get(self.STS_MODEL_NAMES.get(self.sts_model))
        self.money += price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} spent {self.money}"