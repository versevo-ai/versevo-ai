from django.db import models
from engine.settings import AUTH_USER_MODEL

# Create your models here.


class services(models.Model):
   
    # This static choices will be changed from the fetched data of another db model of ML MODEL
    
    TTS_MODEL_NAMES= {
        'TTS_Model1':'tts_model1',
        'TTS_Model2':'tts_model2',
        'TTS_Model3':'tts_model3',
    }
    
    TTS_MODEL_PRICES= {
        'tts_model1':100,
        'tts_model2':200,
        'tts_model3':300,
        'None': 0,
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
        'None': 0,
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
        'None': 0,
    }
    
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="NewUser")
    
    money = models.IntegerField(null=True, blank=True, default=0)
    
    tts_model = models.TextField(choices=TTS_MODEL_NAMES,default='None')
    
    stt_model = models.TextField(choices=STT_MODEL_NAMES,default='None')
    
    sts_model = models.TextField(choices=STS_MODEL_NAMES,default='None')
    
    def save(self, *args, **kwargs):
        temp = 0
        price = self.TTS_MODEL_PRICES.get(self.TTS_MODEL_NAMES.get(self.tts_model))
        temp += price
        
        price = self.STT_MODEL_PRICES.get(self.STT_MODEL_NAMES.get(self.stt_model))
        temp += price
        
        price = self.STS_MODEL_PRICES.get(self.STS_MODEL_NAMES.get(self.sts_model))
        temp += price
        self.money = temp
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} spent {self.money}"