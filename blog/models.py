from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#####################################################################
class BlogPost(models.Model):
    '''
        Defines the content of the blog posts.
    '''
    uid= models.AutoField(primary_key = True , db_index = True)
    title= models.CharField(max_length = 255)
    corpus = models.TextField(blank=True, null=True)
    short_desc= models.CharField(max_length = 255, blank=True, null=True)
    img= models.CharField(max_length = 1000)
    media= models.ManyToManyField('Video', related_name='media_links', blank=True)
    is_visible= models.BooleanField(default= True)
    tags= models.ManyToManyField('Tag', related_name='tags', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    # Methods
    def __str__(self):
        return str(self.title)

#####################################################################
class Video(models.Model):
    '''
        Defines the informations about a video displayed on the site.
    '''
    # choice vars 
    video_source_choices=(
        ('youtube', 'youtube'),
        ('youndcloud', 'soundcloud'),
        ('vimeo', 'vimeo'),
        ('other', 'iframe'),
    )
    # attributes
    uid= models.AutoField(primary_key = True , db_index = True)
    title= models.CharField(max_length = 255)
    thumbnail= models.CharField(
        max_length = 500, blank=True, null=True)
    source_site= models.CharField(max_length = 1000, choices= video_source_choices)
    source_id_string= models.CharField(max_length = 100)
    # Methods
    def __str__(self):
        return str(self.title)
    def colorbox_link(self):
        if self.source_site== 'soundcloud':
            complete_link= 'https://soundcloud.com/{}'.format(self.source_id_string)
        elif self.source_site== 'youtube':
            complete_link= 'https://www.youtube.com/embed/{}'.format(self.source_id_string)
        return complete_link


#####################################################################
class Image(models.Model):
    '''
        Images are a large part of this site. This table keeps track
        of every game image to make their use easy and flexible.
    '''
    uid= models.AutoField(
        primary_key = True , db_index = True)
    title= models.CharField(
        max_length = 255)
    thumbnail= models.CharField(
        max_length = 500, blank=True, null=True)
    full_img=models.CharField(
        max_length = 500, blank=True, null=True)
    external_link= models.CharField(
        max_length = 500, blank=True, null=True)
    legend= models.CharField(
        max_length = 500, blank=True, null=True)
    # Methods
    def __str__(self):
        return str(self.title)

#####################################################################
class Tag(models.Model):
    uid= models.AutoField(primary_key = True , db_index = True)
    title= models.CharField(max_length = 100)
    # Methods
    def __str__(self):
        return str(self.title)

#####################################################################
class Galery(models.Model):
    uid= models.AutoField(primary_key = True , db_index = True)
    title= models.CharField(max_length = 100)
    is_visible= models.BooleanField(default=False)
    img_content= models.ManyToManyField(
        'Image', related_name= 'galery_content', blank= True)
    legend= models.CharField(
        max_length = 500, blank=True, null=True)
    # Methods
    def __str__(self):
        return str(self.title)