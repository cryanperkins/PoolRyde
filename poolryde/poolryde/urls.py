from django.conf.urls import patterns, include, url
from django.contrib import admin
#from blog.views import ArticleTemplate
#from userprofile.views import Index


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
   #url(r'^$', 'poolryde.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^$','signups.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

    #create user profile url
    url(r'^profile/', include('userprofile.urls')),
   # url(r'^test/', Index.as_view()),


url(r'^login/$', 'poolryde.views.login',name='login'),
url(r'^authenticate/$', 'poolryde.views.authenticate', name='authenticate'),
url(r'^logout/$', 'poolryde.views.logout', name='logout'),
url(r'^login_success/$', 'poolryde.views.login_success', name='login_success'),


#urls for registration
url(r'^register/$', 'poolryde.views.register', name='register'),
url(r'^register_success/$', 'poolryde.views.register_success', name='register_success'),


#urls for blog
url(r'^article/$', 'blog.views.article', name='article'),
url(r'^article_template/$', 'blog.views.article_template', name='article_template'),
url(r'^article_template_simple/$', 'blog.views.article_template_simple', name='article_template_simple'),
url(r'^article_class_view/$', 'blog.views.blog_api'),
#url(r'^blog/', include('blog.urls')),

)