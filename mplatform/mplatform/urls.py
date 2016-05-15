from django.conf.urls import include, url
from django.contrib import admin
import xadmin

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/',include(xadmin.site.urls)),
]
