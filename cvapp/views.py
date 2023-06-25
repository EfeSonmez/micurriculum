from django.shortcuts import render, redirect, get_object_or_404
from .models import GeneralSetting, ImageSetting, Skill, Experiences, Educations, Document
# Create your views here.


def layout(request):
    document = Document.objects.all()
    site_title = GeneralSetting.objects.get(name="site_title").parameter
    site_keywords = GeneralSetting.objects.get(name="site_keywords").parameter
    site_description = GeneralSetting.objects.get(name="site_description").parameter
    home_banner_name = GeneralSetting.objects.get(name="home_banner_name").parameter
    home_banner_description = GeneralSetting.objects.get(name="home_banner_description").parameter

    #Images
    header_logo = ImageSetting.objects.get(name="header_logo").file
    home_banner_image = ImageSetting.objects.get(name="home_banner_image").file
    site_favicon = ImageSetting.objects.get(name="site_favicon").file

    context = {
        'document': document,
        'site_title':site_title,
        'site_keywords':site_keywords,
        'site_descriptin':site_description,
        'home_banner_name':home_banner_name,
        'home_banner_description':home_banner_description,
        'header_logo':header_logo,
        'home_banner_image':home_banner_image,
        'site_favicon':site_favicon,
    }
    return context


def index(request):

    #Skill
    skills = Skill.objects.all().order_by("order")

    #experiences
    experiences = Experiences.objects.all().order_by("-start_date")

    #educations
    educations = Educations.objects.all().order_by("edustart_date")

    #Document
    document = Document.objects.all()

    context = {
  
        'skills':skills,
        'experiences':experiences,
        'educations': educations,
    }
    return render(request, 'index.html', context)

def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)


    

