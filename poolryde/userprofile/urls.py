__author__ = 'C. Ryan Perkins'

from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
        # url(r'^$', 'userprofile.views'),
        url(r'^$', 'userprofile.views.user_profile'),
        url(r'edit/$', 'userprofile.views.edit_profile', name='edit_profile'),

)