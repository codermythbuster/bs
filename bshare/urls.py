
from django.contrib import admin
from django.urls import path, include

import home.views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home_view, name='home'),
    path('', include('home.urls', namespace='home')),
    path('',include(('login.urls','login'),namespace='login')),
    path('',include('sell.urls',namespace='sell'))




]
