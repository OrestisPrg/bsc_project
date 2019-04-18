from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome , name='hackme-welcome'),
    path('home/', views.home , name='hackme-home'),
    path('chapters/', views.chapters, name='hackme-chapters'),
    path('about/', views.about, name='hackme-about'),
    path('references/', views.references, name='hackme-references')


]
