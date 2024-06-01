from django.urls import path
from .views import HomePage, AboutPage, LinksPage

urlpatterns = [
    path('', HomePage, name='home'),
    path('about/', AboutPage, name='about'),
    path('links/', LinksPage.as_view(), name='links')
]