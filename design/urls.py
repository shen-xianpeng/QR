from django.conf.urls import patterns, include, url
from django.conf import settings
from .views import IndexView
from notifications.views import NotificationView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^user/', include('users.urls')),
    url(r'^question/', include('questions.urls')),
    url(r'^notifications/', NotificationView.as_view(), name='design-notification'),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
   urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
           url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}), )
