from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

def costume_photo_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

def reference_photo_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.

class Costume(models.Model):
    character = models.CharField(max_length=200)
    series = models.CharField(max_length=200)
    variant = models.CharField(max_length=200)
    notes = models.TextField()
    cosplayer = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    def __str__(self):
        return self.series + ' - ' + self.character + ' [' + self.variant + '] '

class Component(models.Model):
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    notes = models.TextField()

class ReferencePhoto(models.Model):
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=reference_photo_path, height_field=None, width_field=None, max_length=100)

class CostumePhoto(models.Model):
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=costume_photo_path, height_field=None, width_field=None, max_length=100)
