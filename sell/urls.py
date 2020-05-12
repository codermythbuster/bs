from django.urls import path

from . import views

urlpatterns = [
    path('sell/', views.personal_info, name='sell'),

]
