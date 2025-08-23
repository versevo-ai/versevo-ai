from django.urls import path, include
from services.views import *
from versemodels.views import *
from django.contrib.auth.decorators import login_required

# ML Model management and monitoring endpoints
# User management is now handled by FastAPI

urlpatterns = [
    # Remove user endpoint - now handled by FastAPI
    # path("users/", userViews.as_view()),
    path("services/", login_required(serviceViews.as_view())),  # Will add those PKs later
    path("models/",login_required(VersevoModelViews.as_view())), # Will add those PKs later
    path("chat/",login_required(VersevoModelViews.as_view()))   # Will add those PKs later
]
