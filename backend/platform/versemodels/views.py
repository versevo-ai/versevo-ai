from django.http import JsonResponse
from django.views import View
from .models import *
from .forms import *
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class VersevoModelViews(LoginRequiredMixin,View):
    def get(self, request,Mtags=None,Mname=None):
        try:
            if Mtags or Mname:
                if ChatModels.objects.filter(Mname=Mname).exists()==True:
                    return JsonResponse({
                        "Message":"FETCHED",
                        "Data":f"{serialize('json',ChatModels.objects.filter(Mname=Mname).all())}"
                    })
                else:
                    return JsonResponse({"Message":"Incorrect Parameters"})
            else:
                return JsonResponse({
                    "Message":"FETCHED",
                    "Data":f"{serialize('json',ChatModels.objects.all())}"
                })
        except Exception as e:
            return JsonResponse({
                "Message":f"Error Occured - {e}"
            })
    
    def post(self,request):
        FormObject = ChatModelsForm(request.POST or None)
        try:
            if FormObject.is_valid():
                dict_data = FormObject.cleaned_data
                obj = ChatModels(**dict_data)
                if ChatModels.objects.filter(Mname=obj.Mname).exists() == False:
                    obj.save()
                    return JsonResponse({
                        "Message":"CREATED",
                        "Data":f"{serialize('json',obj)}"
                    })
                else:
                    obj.save()
                    obj.update_and_save()
                    return JsonResponse({
                        "Message":"UPDATED",
                        "Data":f"{serialize('json',obj)}"
                    })
        except Exception as e:
            return JsonResponse({"Message":"ERROR","Message":f"{e}"})

    
    def delete(self,request,Mtags=None,Mname=None):
        if Mtags or Mname:
            if ChatModels.objects.filter(Mname=Mname).exists()==True:
                ChatModels.objects.get(Mname=Mname).delete()
                return JsonResponse({"Message":"ML Model Deleted"})
            else:
                return JsonResponse({"Message":"Incorrect Parameters"})
        else:
            return JsonResponse({"Message":"Parameters Can't be None"})


class ChatwithModelViews(LoginRequiredMixin,View):
    def get(self,request,username,Mname,chat_no:None):
        try:
            pass
        except Exception as e:
            pass
    
    def post(self,request):
        Formobject = ModelRequestResponseForm(request.POST or None)
        try:
            pass
        except Exception as e:
            pass
    def delete(self,request,chat_no:None):
        pass