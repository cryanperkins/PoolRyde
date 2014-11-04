from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
   #url(r'^$', 'poolryde.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^$','signups.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),




url(r'^login/$','poolryde.views.login',name='login'),
url(r'^authenticate/$', 'poolryde.views.authenticate', name='authenticate'),
url(r'^logout/$', 'poolryde.views.logout', name='logout'),
url(r'^login_success/$', 'poolryde.views.login_success', name='login_success'),
#url(r'^login_fail/$', 'poolryde.views.login_fail', name='login_fail'),

#urls for registration
url(r'^register/$','poolryde.views.register',name='register'),
url(r'^register_success/$', 'poolryde.views.register_success', name='register_success'),

)