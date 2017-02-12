from django.contrib import admin
from .models import *

class AdminBlogPost(admin.ModelAdmin):
    list_display =['uid','title']
    ordering = ['uid']
admin.site.register(BlogPost, AdminBlogPost)

class AdminVideo(admin.ModelAdmin):
    list_display =['uid','title', 'source_id_string']
    ordering = ['uid']
admin.site.register(Video, AdminVideo)

class AdminTag(admin.ModelAdmin):
    list_display =['uid','title']
    ordering = ['uid']
admin.site.register(Tag, AdminTag)

class AdminImage(admin.ModelAdmin):
    list_display =['uid','title']
    ordering = ['uid']
admin.site.register(Image, AdminImage)

class AdminGalery(admin.ModelAdmin):
    list_display =['uid','title']
    ordering = ['uid']
admin.site.register(Galery, AdminGalery)