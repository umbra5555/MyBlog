from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'MyBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ed.urls',  namespace="ed")),
    #url(r'^', include('polls.urls',  namespace="polls"))
    #url(r'^', include('blog.urls')),
    #url(r'^articles/(?P<article_id>[0-9]+)/$', 'blog.views.show_article', name = 'article')
]
