from django.urls import path, include
from users.views import *
from services.views import *
from django.contrib.auth.decorators import login_required

# will have class based views , so will put classnames.as_view() instead of include

urlpatterns = [
    path("users/", userViews.as_view()),
    path("services/", login_required(serviceViews.as_view())),
]
