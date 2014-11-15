__author__ = 'C. Ryan Perkins'

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
       # url(r'^$', 'userprofile.views'),
        url(r'^$', 'userprofile.views.user_profile'),
        url(r'^edit_profile/$', 'userprofile.views.edit_profile'),

)