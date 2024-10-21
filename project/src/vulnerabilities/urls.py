from django.urls import path
from .views import homePageView, injectionPageView, adminPageView

# Urls

urlpatterns = [
    path('', homePageView, name='home'),
    path('injection/', injectionPageView, name='injection'),
    path('admin_only/', adminPageView, name='admin_only')
]
