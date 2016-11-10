from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /costumes/5/
    url(r'^(?P<costume_id>[0-9]+)/$', views.costumepage, name='costumepage'),
]
