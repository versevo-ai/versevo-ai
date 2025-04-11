from django import forms
from .models import *

class ModelRequestResponseForm(forms.ModelForm):
    class Meta:
        model = ModelRequestResponse
        fields = ["page_no","chat_no","question","answer"]