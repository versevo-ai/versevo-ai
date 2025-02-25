from django.db import models

from engine.settings import AUTH_USER_MODEL

# Create your models here.

class ChatModels(models.Model):   # This model will populate data at /EXPLORE-MODELS/ page
    CATEGORY = {
        "Text-To-Speech":"Text-To-Speech",
        "Speech-To-Text":"Speech-To-Text",
        "Speech-to-Speech":"Speech-to-Speech"
    }
    Mname = models.CharField(primary_key=True)
    Mnewname = models.CharField(null=True,blank=True)   #  Will not be shown in Frontned
    Mcategory = models.TextField(choices=CATEGORY)
    Mparams = models.CharField()
    Mtags = models.CharField()
    Mdescription = models.CharField()
    Mprice = models.DecimalField(decimal_places=2)
    
    def update_and_save(self):
        obj = ChatModels.objects.get(Mname=self.Mname)
        if self.Mnewname != obj.Mname:
            obj.Mname = self.Mnewname
        if obj.Mcategory != self.Mcategory:
            obj.Mcategory = self.Mcategory
        if obj.Mparams != self.Mparams:
            obj.Mparams = self.Mparams
        if obj.Mtags != self.Mtags:
            obj.Mtags = self.Mtags
        if obj.Mprice != self.Mprice:
            obj.Mprice = self.Mprice
        obj.save()
        
    
    def __str__(self):
        return f"{self.Mname} of {self.Mcategory}"


# This model will store  user's query and response with a ML Model
class ModelRequestResponse(models.Model):   # After WS connection and room creation , this db model will control query-response cycle
    
    # This model is dependent on User Model but will be filled up manually
    
    username = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="NewUser")
    Mname = models.ForeignKey(ChatModels,on_delete=models.SET_NULL,related_name="ChatModels")
    chat_no = models.IntegerField()
    question = models.CharField()
    answer = models.CharField()
    
    def __str__(self):
        return f"{self.username} - {self.Mname} - {self.count}"
    
    