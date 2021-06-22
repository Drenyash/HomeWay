from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name='about'),
    path('404', views.error, name='not_found'),
    path('work', views.work, name='work')
]