from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import liighter_app.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', include('liighter_app.urls')),
    url(r'^db', liighter_app.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
