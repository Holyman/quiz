from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

import views

urlpatterns = patterns('',
	url(r'^$', views.home),
	url(r'submit/$', views.submit),
	url(r'^accounts/login/$', login),
	url(r'^logout/$', views.logout_view)
	)