from django.shortcuts import render
from .models import GeneralSetting
# Create your views here.

def index(request):
    site_title = GeneralSetting.objects.get(name="site_title").parameter
    site_keywords = GeneralSetting.objects.get(name="site_keywords").parameter
    site_description = GeneralSetting.objects.get(name="site_description").parameter
    home_banner_name = GeneralSetting.objects.get(name="home_banner_name").parameter
    home_banner_description = GeneralSetting.objects.get(name="home_banner_description").parameter

    context = {
        'site_title':site_title,
        'site_keywords':site_keywords,
        'site_descriptin':site_description,
        'home_banner_name':home_banner_name,
        'home_banner_description':home_banner_description
    }
    return render(request, 'index.html', context)

