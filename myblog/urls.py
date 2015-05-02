from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'apps.blog.views.index', name='index'),
    url(r'^add_blog/', 'apps.blog.views.add_blog', name='add_blog'),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    url(r'^(?P<id>\d+)/', 'apps.blog.views.type_blog', name='type_blog'),
    url(r'^type/(?P<id>\d+)/', 'apps.blog.views.type_id', name='type_id'),
    url(r'^profile/', 'apps.blog.views.profile', name='profile'),
    url(r'^logout/$', 'apps.blog.views.user_logout', name='logout'),
    url(r'^login/$', 'apps.blog.views.login', name='login'),
    url(r'^delete/(?P<id>\d+)/$', 'apps.blog.views.delete', name='delete'),
    url(r'^register/', 'apps.blog.views.register', name='register'),
    # Examples:
    # url(r'^$', 'testdrive.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
