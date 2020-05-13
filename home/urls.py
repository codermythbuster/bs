from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from.import views

from .views import BookViewSet, aboutus

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
app_name = 'home'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('', include('sell.urls')),
    path('aboutus', aboutus, name='about'),
    path('cart/',views.cart,name='cart'),

]
