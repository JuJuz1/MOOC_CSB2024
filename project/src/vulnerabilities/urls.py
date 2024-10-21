from django.urls import path
from .views import homePageView, injectionPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('injection/', injectionPageView, name='injection'),
]
