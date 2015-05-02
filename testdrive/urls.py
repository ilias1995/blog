from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'apps.tests.views.index', name='index'),
    url(r'^add_blog/', 'apps.tests.views.add_blog', name='add_blog'),
    url(r'^blog/', include('apps.tests.urls', namespace='blog')),
    url(r'^(?P<id>\d+)/', 'apps.tests.views.type_blog', name='type_blog'),
    url(r'^type/(?P<id>\d+)/', 'apps.tests.views.type_id', name='type_id'),
    url(r'^profile/', 'apps.tests.views.profile', name='profile'),
    url(r'^logout/$', 'apps.tests.views.user_logout', name='logout'),
    url(r'^login/$', 'apps.tests.views.login', name='login'),
    url(r'^delete/(?P<id>\d+)/$', 'apps.tests.views.delete', name='delete'),
    # Examples:
    # url(r'^$', 'testdrive.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
