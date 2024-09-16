from django.views import View
from .serializers import *
from .models import *
from services.models import *
from .forms import *
from django.core.serializers import serialize
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class userViews(LoginRequiredMixin, View):
    def get(self, request, username):

        """
        Method to GET Data from Server
        """

        # Tokens will be fetched from Security Module and then verification will be done in GET Request

        if NewUser.objects.get(username=username):
            user_data = serialize(
                "json", NewUser.objects.filter(username=username).all()
            )
            return user_data
        else:
            return JsonResponse({"Status":"ERROR","Message":f"username {username} already exists"})

    def post(self, request):

        """
        Method to POST fresh Data to Server
        """
        userform_data = UserForm(request.POST or None)
        try:
            if userform_data.is_valid():
                password = userform_data.clean_password2()
                fetched_data = userform_data.cleaned_data
                raw_user_data = UserModelSerializer(
                    username=fetched_data.get("username"),
                    email=fetched_data.get("email"),
                    password=password,
                    first_name=fetched_data.get("first_name"),
                    last_name=fetched_data.get("last_name"),
                )
                if raw_user_data==True:
                    if raw_user_data.method in ['POST','post']:
                        obj = raw_user_data.create_user_api()
                        user_obj = NewUser.objects.filter(username=fetched_data.get("username")).all()
                        login(request, user_obj)
                        return obj
                    elif raw_user_data.method in ['PUT','put','PATCH','patch']:
                        if (raw_user_data.password != NewUser.objects.get(username=request.user.username).password):
                            form = PasswordChangeForm(user=request.user, data=raw_user_data.password)
                            try:
                                if form.is_valid():
                                    form.save()
                                    update_session_auth_hash(request, form.user)
                                    obj = raw_user_data.update_user_api() 
                                    return obj
                            except Exception:
                                return JsonResponse({"Message": "Password is not Valid"})
                        else:
                            obj = raw_user_data.update_user_api(username=raw_user_data.username) 
                            return obj
                else:
                    return raw_user_data.throw_errorlist()
        except Exception:
            return JsonResponse({"Status":"ERROR","Message":"Invalid Data in Form"})


    def delete(self, request):
        """
        Method to DELETE an user's data
        """
        try:
            if request.user is not None:
                uname = request.user.username
                if NewUser.objects.get(username=uname).Blacklisted:
                    NewUser.objects.filter(username=uname).all().delete()
                    logout(request)
                    return {"Message": f"User Object of Username {uname} is deleted"}
        except Exception:
            return JsonResponse({"Status":"ERROR","Message":"User Does Not Exists"})