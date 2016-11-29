from django.conf.urls import url
from . import views #this means we are importing views from current package


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
