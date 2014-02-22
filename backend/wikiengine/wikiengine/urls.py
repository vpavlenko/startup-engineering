from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'articles.views.home', name='home'),
    url(r'^([A-Za-z0-9 ]+)/$', 'articles.views.show_article', name='show'),
    url(r'^([A-Za-z0-9 ]+)/edit/$', 'articles.views.edit_article', name='edit'),
    url(r'^save_article$', 'articles.views.save_article', name='save'),
    url(r'^create_article$', 'articles.views.create_article', name='create'),
    # url(r'^blog/', include('blog.urls')),
)
