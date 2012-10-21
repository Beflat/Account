from django.conf.urls import url, patterns

urlpatterns = patterns('account.views', 
    url(r'^$', 'index'),
    url(r'^batch/$', 'batch', name='batch'),
    url(r'^new/$', 'new'),
    url(r'^register/$', 'register'),
)
