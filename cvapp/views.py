from django.shortcuts import render, redirect, get_object_or_404
from .models import GeneralSetting, ImageSetting, Skill, Experiences, Educations, Document
# Create your views here.

def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name="parameter").parameter
    except GeneralSetting.DoesNotExist:
        obj = ''

    return obj

def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name="parameter").file
    except ImageSetting.DoesNotExist:
        obj = ''

    return obj



def layout(request):
    document = Document.objects.all()
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_description = get_general_setting('home_banner_description')

    #Images
    header_logo = get_image_setting('header_logo')
    home_banner_image = get_image_setting('home_banner_image')
    site_favicon = get_image_setting('site_favicon')

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


    

