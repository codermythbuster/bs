
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import home.views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home_view, name='home'),
    path('', include('home.urls', namespace='home')),
    path('',include(('login.urls','login'),namespace='login')),
    path('',include('sell.urls',namespace='sell'))

]
if settings.DEBUG == True :
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)