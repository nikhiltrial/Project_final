from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from bugfixer import views

urlpatterns = [
    url('admin/', admin.site.urls),
    path('bugfixer/', include('bugfixer.urls')),
    url(r'^$', views.redirect, name='redirect'),
]
