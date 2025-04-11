from django.http import JsonResponse
from django.views import View
from .models import *
from .forms import *
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import NewUser

# Create your views here.

class VersevoModelViews(LoginRequiredMixin,View):
    def get(self, request,Mtags=None,Mname=None):
        try:
            if Mtags or Mname:
                obj = ChatModels.objects.filter(Mname=Mname)
                if obj.exists()==True:
                    return JsonResponse({
                        "Message":"FETCHED",
                        "Data":f"{serialize('json',obj.all())}"
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



class ChatwithModelViews(LoginRequiredMixin,View):
    def get(self,request,Mname,page_no,chat_no=None):
        try:
            if chat_no is not None:
                obj = ModelRequestResponse.objects.filter(
                    username = NewUser.objects.get(username = request.user.username),
                    Mname = ChatModels.objects.get(Mname=Mname),
                    page_no = page_no,
                    chat_no = chat_no
                )
                if obj.exists()==True:
                    return JsonResponse({
                        "Message":"FETCHED",
                        "Data":f"{serialize('json',obj.all())}"
                    })
                else:
                    return JsonResponse({"Message":"Incorrect Parameters"})
            else:
                obj = ModelRequestResponse.objects.filter(
                    username = NewUser.objects.get(username = request.user.username),
                    Mname = ChatModels.objects.get(Mname=Mname),
                    page_no = page_no
                )
                if obj.exists()==True:
                    return JsonResponse({
                        "Message":"FETCHED",
                        "Data":f"{serialize('json',obj.all())}"
                    })
                else:
                    return JsonResponse({"Message":"Incorrect Parameters"})
        except Exception as e:
            return JsonResponse({
                "Message":f"Error Occured - {e}"
            })
    
    def post(self,request,Mname):
        Formobject = ModelRequestResponseForm(request.POST or None)
        try:
            if Formobject.is_valid():
                data = Formobject.cleaned_data
                if ModelRequestResponse.objects.filter(
                    username = NewUser.objects.get(username=request.user.username),
                    Mname = ChatModels.objects.get(Mname=Mname),
                    page_no = data.get("page_no"),
                    chat_no = data.get("chat_no"),
                ).exists():
                    obj = ModelRequestResponse.objects.get(
                    username = NewUser.objects.get(username=request.user.username),
                    Mname = ChatModels.objects.get(Mname=Mname),
                    page_no = data.get("page_no"),
                    chat_no = data.get("chat_no")
                )
                    obj.question = data.get("question")
                    obj.answer = data.get("answer")
                    obj.save()
                    return JsonResponse({
                        "Message":"UPDATED",
                        "Data":f"{serialize('json',obj)}"
                    })
                else:
                    obj = ModelRequestResponse(
                        username = NewUser.objects.get(username=request.user.username),
                        Mname = ChatModels.objects.get(Mname=Mname),
                        page_no = data.get("page_no"),
                        chat_no = data.get("chat_no"),
                        question = data.get("question"),
                        answer = data.get("answer")
                    )
                    obj.save()
                    return JsonResponse({
                        "Message":"CREATED",
                        "Data":f"{serialize('json',obj)}"
                    })
            else:
                return JsonResponse({"Message":"Invalid Data in Form"})
        except Exception as e:
            return JsonResponse({"Message":f"ERROR-f{e}"})
    

    
    def delete(self,request,Mname,page_no,chat_no=None):
        try:
            if chat_no is not None:
                obj = ModelRequestResponse.objects.filter(
                    username = NewUser.objects.get(username = request.user.username),
                    Mname = ChatModels.objects.get(Mname=Mname),
                    page_no = page_no,
                    chat_no = chat_no
                ).all()
                obj.delete()
                return JsonResponse({"Message":"Chat Removed"})
            else:
                obj = ModelRequestResponse.objects.filter(
                    username = NewUser.objects.get(username = request.user.username),
                    Mname = ChatModels.objects.get(Mname=Mname),
                    page_no = page_no
                ).all()
                obj.delete()
                return JsonResponse({"Message":"Page of chats removed"})
        except ModelRequestResponse.DoesNotExist:
            return JsonResponse({"Message":"ERROR","Message":"No Information related to this chat/s"})
        except Exception as e:
            return JsonResponse({"Message":"ERROR","Message":f"{e}"})