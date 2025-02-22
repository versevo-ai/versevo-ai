from django.http import JsonResponse
from django.views import View
from .serializers import *
from .models import *
from .forms import *
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import NewUser

# Create your views here.


class serviceViews(LoginRequiredMixin, View):
    def get(self, request, username):
        """
        Method to GET Data from Server
        """
        if services.objects.get(username=username):
            user_data = serialize(
                "json", services.objects.filter(username=username).all()
            )
            return user_data
        else:
            return JsonResponse({"Message": "Data Not Found"})

    def post(self, request):
        """
        Method to POST fresh Data to Server
        """
        serviceform_data = UserServiceForm(request.POST or None)
        try:
            if serviceform_data.is_valid():
                fetched_data = serviceform_data.cleaned_data
                if services.objects.filter(user=fetched_data.get(id)).exists() == False:
                    obj = services(
                        **fetched_data
                    )
                    obj.save()
                    return JsonResponse({"Status":201 , "Data":f"{serialize("json",obj)}"})
                else:
                    prev_obj = services.objects.get(user=fetched_data.get(id))
                    if prev_obj.tts_model != fetched_data.get("tts_model"):
                        prev_obj.tts_model = fetched_data.get("tts_model")
                    if prev_obj.stt_model != fetched_data.get("stt_model"):
                        prev_obj.stt_model = fetched_data.get("stt_model")
                    if prev_obj.sts_model != fetched_data.get("sts_model"):
                        prev_obj.sts_model = fetched_data.get("sts_model")
                    prev_obj.save()
                    return JsonResponse({"Status":200 , "Data":f"{serialize("json",prev_obj)}"})
        except Exception:
            return JsonResponse({"Status":"ERROR","Message":"Invalid Data in Form"})

    def delete(self, request, username):
        """
        Method to DELETE an user's data
        """
        try:
            if username and services.objects.filter(username=username):
                services.objects.filter(username=username).all().delete()
                return JsonResponse({"Message": f"Data of {username} is deleted"})
        except Exception:
            return JsonResponse({"Message":"User Does not Exists"})
