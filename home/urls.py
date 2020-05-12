from django.conf.urls import url, include
from rest_framework import routers

from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
app_name = 'home'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
