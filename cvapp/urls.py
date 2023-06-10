from django.urls import path,include
from cvapp.views import index

urlpatterns = [
    path("", index, name='index'),
]