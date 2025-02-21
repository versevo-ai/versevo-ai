from django.core.serializers import serialize
from django.http import JsonResponse
# from django.core.exceptions import ValidationError
from .models import services


class ServiceModelSerializer:
    """
    This Serializer is used to Serialize Raw Data of Services Model into REST API (JSON)
    """

    def __init__(self, username, money, text_to_speech, speech_to_text, speech_to_speech, method:str , new_username:str=None) -> None:
        self.username = username
        self.new_username = new_username
        self.money = money
        self.method = method
        self.text_to_speech = text_to_speech
        self.speech_to_text = speech_to_text
        self.speech_to_speech = speech_to_speech

    def create_service_api(self):
        serve_obj = services.objects.create(
            username=self.username,
            money=self.money,
            text_to_speech=self.text_to_speech,
            speech_to_text=self.speech_to_text,
            speech_to_speech=self.speech_to_speech,
        )
        service_api = serialize("json", serve_obj)
        return service_api

    def update_service_api(self, username):
        serve_obj = services.objects.get(username=username)
        if serve_obj:
            if serve_obj.username != self.new_username:
                serve_obj.username = self.new_username

            if serve_obj.money != self.money:
                serve_obj.money = self.money

            if serve_obj.text_to_speech != self.text_to_speech:
                serve_obj.text_to_speech = self.text_to_speech

            if serve_obj.speech_to_text != self.speech_to_text:
                serve_obj.speech_to_text = self.speech_to_text

            if serve_obj.speech_to_speech != self.speech_to_speech:
                serve_obj.speech_to_speech = self.speech_to_speech
            serve_obj.save()
            serve_api = serialize("json", serve_obj)  # type: ignore
            return serve_api
        else:
            return JsonResponse({"Status":"ERROR","Message":f"User Does Not Exists"})
    
    def throw_errorlist(self):
        return self.messagstack
