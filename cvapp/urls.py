from django.urls import path,include
from cvapp.views import index, contact

urlpatterns = [
    path("", index, name='index'),
    path("contact/", contact, name='contact'),
]