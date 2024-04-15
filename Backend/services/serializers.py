from django.core.serializers import serialize , deserialize
from django.core.exceptions import ValidationError
from .models import services

class ServiceModelSerializer:
    def __init__(self,username,money,text_to_speech,speech_to_text,speech_to_speech) -> None:
        self.model = services
        self.username = username
        self.money = money
        self.text_to_speech = text_to_speech
        self.speech_to_text = speech_to_text
        self.speech_to_speech = speech_to_speech

    
    def create_service_api(self):
        serve_obj = self.model.objects.create(
            username = self.username , money = self.money , text_to_speech = self.text_to_speech , speech_to_text = self.speech_to_text , speech_to_speech = self.speech_to_speech  
        )
        service_api = serialize("json",serve_obj)
        return service_api
    
    
    def update_service_api(self,username):
        serve_obj = self.model.objects.get(username = username)
        if serve_obj.username != self.username:
            serve_obj.username = self.username
            
        if serve_obj.money != self.money:
            serve_obj.money = self.money
            
        if serve_obj.text_to_speech != self.text_to_speech:
            serve_obj.text_to_speech = self.text_to_speech
            
        if serve_obj.speech_to_text != self.speech_to_text:
            serve_obj.speech_to_text = self.speech_to_text
            
        if serve_obj.speech_to_speech != self.speech_to_speech:
            serve_obj.speech_to_speech = self.speech_to_speech
        serve_obj.save()
        serve_api = serialize("json",serve_obj) 
        return serve_api