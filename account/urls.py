from django.conf.urls import url, patterns

urlpatterns = patterns('account.views', 
                       url(r'^$', 'index'),
                       )
