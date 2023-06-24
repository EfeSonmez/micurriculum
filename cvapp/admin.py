from django.contrib import admin
from cvapp.models import *
# Register your models here.

@admin.register(GeneralSetting)

class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date','created_date']
    search_fields = ['name', 'description','parameter']
    list_editable = ['description', 'parameter']
    
    class Meta:
        model = GeneralSetting

@admin.register(ImageSetting)

class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date','created_date']
    search_fields = ['name', 'description','file']
    list_editable = ['description', 'file']
    
    class Meta:
        model = ImageSetting

@admin.register(Skill)

class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','order', 'backendname','frontname','pmname','percentage','percentage3','percentage4', 'updated_date','created_date']
    search_fields = ['backendname','frontname','pmname',]
    list_editable = ['percentage','percentage3','percentage4','backendname','frontname','pmname', 'order']
    
    class Meta:
        model = Skill

@admin.register(Experiences)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','job_title','job_location','start_date','end_date']
    search_fields = ['company_name','job_title','job_location']
    list_editable = ['company_name','job_title','job_location','start_date','end_date']
    
    class Meta:
        model = Experiences

@admin.register(Educations)

class EducationsAdmin(admin.ModelAdmin):
    list_display = ['id','uni_name','edu_title','edu_location','edustart_date','eduend_date']
    search_fields = ['uni_name','edu_title','edu_location']
    list_editable = ['uni_name','edu_title','edu_location','edustart_date','eduend_date']
    
    class Meta:
        model = Educations