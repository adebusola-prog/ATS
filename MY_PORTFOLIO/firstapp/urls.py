from django.urls import path
from firstapp.views import homepage


urlpatterns = [
    path("", homepage, name="homepage"),
]