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
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'cosplayer', None) is None:
            obj.cosplayer = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(CostumeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(cosplayer=request.user)

admin.site.register(Costume, CostumeAdmin)
