from django.conf.urls import url
from mainapp import views
urlpatterns = [
    url(r'^$', "mainapp.views.index", name='index'),
]
