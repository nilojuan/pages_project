# pages/urls.py

from django.urls import path

from .views import HomePageView, AboutPageView, CovidPageView # new # new

urlpatterns = [
path('covid/', CovidPageView.as_view(), name='covid'), # new   
path('about/', AboutPageView.as_view(), name='about'), # new
path('', HomePageView.as_view(), name='home'),
]