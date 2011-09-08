from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('polls.views',
      (r'^polls/$', 'index'),
      (r'^polls/(?P<poll_id>\d+)/$', 'detail'),
      (r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
      (r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
)

urlpatterns += patterns('',
	url(r'^admin/', include(admin.site.urls)),
)
