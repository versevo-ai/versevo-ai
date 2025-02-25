from django import forms
from .models import *

class ChatModelsForm(forms.ModelForm):
    class Meta:
        model = ChatModels
        fields = "__all__"

class ModelRequestResponseForm(forms.ModelForm):
    class Meta:
        model = ModelRequestResponse
        fields = ["question","answer"]