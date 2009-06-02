from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', dict(template='account_index.html')),
    (r'^sorry/$', 'django.views.generic.simple.direct_to_template', dict(template='account_nam.html'), 'muaccounts_not_a_member'),
    (r'^accounts/login/', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/', 'django.contrib.auth.views.logout', dict(next_page='/')),
    (r'^admin/', include('muaccounts.urls')),
)
