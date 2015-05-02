from django.conf.urls.defaults import *
from django.contrib import admin
import dbindexer
from django.conf.urls.static import static
import settings
handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns(

    '',
     (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                            { 'document_root' : settings.MEDIA_ROOT,
                              'show_indexes'  : True }
                            ),
    url(r'^mainapp/', include('mainapp.urls')),

    url(r'^login/', include('security.urls')),
    url(r'^loans/', include('loan.urls')),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'mainapp.views.index'),
    ('^admin/', include(admin.site.urls)),
    
)
