from django.contrib import admin

# Register your models here.

from .models import Costume, Component, ReferencePhoto, CostumePhoto 

class RefInline(admin.StackedInline):
    model = ReferencePhoto
    extra = 3

class PhotoInline(admin.StackedInline):
    model = CostumePhoto
    extra = 3

class ComponentInline(admin.StackedInline):
    model = Component
    extra = 3

class CostumeAdmin(admin.ModelAdmin):

    inlines = [RefInline, PhotoInline, ComponentInline]

admin.site.register(Costume, CostumeAdmin)
