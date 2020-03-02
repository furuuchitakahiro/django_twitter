from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework import routers
import debug_toolbar

from tweets.views import TweetViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('tweets', TweetViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
