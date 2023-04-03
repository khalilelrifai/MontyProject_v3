
from django.contrib import admin
from django.urls import include, path, re_path


urlpatterns = [

    path('', include('home.urls')), 
    path('ads/', include('ads.urls')),
    path('admin/', admin.site.urls),  # Keep
    # path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^keycloak/', include('django_keycloak.urls')),



]

