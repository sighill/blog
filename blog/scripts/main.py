#python3 main.py

#####################################################################
def CreateGalery(directory):
    '''
        Allows an user to automatically create a galery of images
        on the database, linked to eveyr image of a folder in the
        server. The bulk create gives placeholder names and no
        links. An other interface is built to easily modify the data.
    '''
from blog.models import *
from os import listdir
from os.path import isfile, join, splitext
from pathlib import Path
# get every file of the directory
images = [f for f in listdir(directory) if isfile(join(directory, f))]

# create every image and append them to a list
img_obj_array=[]
for img in images:
    new= Image()
    new.title= splitext(img)[0]
    new.thumbnail= join(directory, '{}.thumbnail'.format(splitext(img)[0]))
    new.full_img= join(directory, img)
    img_obj_array.append(new)
# Bulk create the objects using django's bulk_create
Image.objects.bulk_create(img_obj_array)
# the array is used to create the galery AND the links
new_galery= Galery()
new_galery.title= Path(directory).parts[-1]
new_galery.save()

# now we bulk add the relation
for obj in img_obj_array:
    obj.save()
    new_galery.img_content.add(obj)