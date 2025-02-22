from django import forms
from .models import services


class UserServiceForm(forms.ModelForm):
    class Meta:
        model = services
        fields = ['tts_model','stt_model','sts_model']
