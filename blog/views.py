from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *

#####################################################################
def FrontPage(request):
    '''
        Landing page for the whole blog.
    '''
    last_medias= Video.objects.select_related().all()[:3]
    for media in last_medias:
        media.colorbox_link= media.colorbox_link()
    context={
        'style': '/static/blog/style.css',
        'last_articles': BlogPost.objects.select_related().all()[:3],
        'last_galeries': Galery.objects.select_related().all()[:3],
        'last_medias': last_medias,
    }
    template = loader.get_template('frontpage.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def ArticleIndex(request):
    '''
        Index of articles.
    '''
    context={
        'blogposts': BlogPost.objects.filter(is_visible=True),
        'style': '/static/blog/style.css',
        'all_tags': Tag.objects.all(),
    }
    template = loader.get_template('article_index.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def ArticleView(request, article_pk):
    '''
        View a single article.
    '''
    context={
        'post': BlogPost.objects.select_related().get(pk= article_pk),
        'style': '/static/blog/style.css',
    }
    template = loader.get_template('article_view.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def GaleryIndex(request):
    '''
        Index of articles.
    '''
    context={
        'galeries': Galery.objects.select_related().filter(is_visible=True),
        'style': '/static/blog/style.css',
    }
    template = loader.get_template('galery_index.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def GaleryView(request, galery_pk):
    '''
        View a single galery and its content.
    '''
    context={
        'gal': Galery.objects.select_related().get(pk=galery_pk),
        'style': '/static/blog/style.css',
    }
    template = loader.get_template('galery_view.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def SonsIndex(request):
    '''
        Index of sounds.
    '''
    sons= Video.objects.all()
    for son in sons:
        son.colorbox_link= son.colorbox_link()
    context={
        'sons': sons,
        'style': '/static/blog/style.css',
    }
    template = loader.get_template('sons_index.html')
    return HttpResponse(template.render(context, request))