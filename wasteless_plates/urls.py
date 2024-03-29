from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('wasteless_plates.home.urls')),
    url(r'^recipes/', include('wasteless_plates.recipes.urls'))
)
