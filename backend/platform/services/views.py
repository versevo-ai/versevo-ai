from django.http import JsonResponse
from django.views import View
from .models import *
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from versemodels.models import ChatModels

# Create your views here.

# Whenever user will do any operation with the Versemodels at /EXPLORE/ , this view will work

class serviceViews(LoginRequiredMixin, View):
    def get(self, request):
        try:
            return JsonResponse({
                "Message":"FETCHED",
                "Data":f"{serialize('json',services.objects.filter(username=request.user).all())}"
            })
        except Exception as e:
            return JsonResponse({
                "Message":f"Error Occured - {e}"
            })

    def post(self, request,Mname):
        # WHENEVR PURCHASE HAPPENS , SERVICE OBJECT GET CREATED
        try:
            if services.objects.filter(username=request.user).exists()==False:
                model_obj = ChatModels.objects.get(Mname=Mname)
                service_obj = services(**model_obj)
                service_obj.save()
                return JsonResponse({
                    "Message":"CREATED",
                    "Data":f"{serialize('json',service_obj)}"
                })
            else:
                model_obj = ChatModels.objects.get(Mname=Mname)
                service_obj = services.objects.get(username=request.user,Mname=model_obj) 
                service_obj.Mname = model_obj
                service_obj.Mcategory = model_obj.Mcategory
                service_obj.Mparams = model_obj.Mparams
                service_obj.Mtags = model_obj.Mtags
                service_obj.Mdescription = model_obj.Mdescription
                service_obj.Mprice = model_obj.Mprice
                service_obj.save()
                return JsonResponse({
                    "Message":"UPDATED",
                    "Data":f"{serialize('json',service_obj)}"
                })
        except Exception as e:
            return JsonResponse({"Message":"ERROR","Message":f"{e}"})

    def delete(self, request, Mname):
        try:
            services.objects.filter(username=request.user , Mname=ChatModels.objects.get(Mname=Mname)).all().delete()
            return JsonResponse({"Message":"Service Removed"})
        except Exception as e:
            return JsonResponse({"Message":"ERROR","Message":f"{e}"})
