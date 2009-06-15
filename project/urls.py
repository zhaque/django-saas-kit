from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

import signal_handlers
signal_handlers.install()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', dict(template='index.html')),
    (r'^accounts/', include('registration.urls')),
    (r'^accounts/mua/', include('muaccounts.urls')),
    (r'^sub/', include('subscription.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)
