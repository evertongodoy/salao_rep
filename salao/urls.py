from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    # url (r'^$', 'TaskManager.views.page'),
    url(r'^', include('core.urls', namespace='grupoCore')), # namespace eh um grupo de URL e eh usado em conjunto com o include
    url(r'^admin/', include(admin.site.urls)),
)