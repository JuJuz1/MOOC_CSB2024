from django.urls import path
from .views import homePageView, searchPageView, adminPageView, secureDataPageView

# Urls

urlpatterns = [
    path('', homePageView, name='home'),
    path('search/', searchPageView, name='search'),
    path('admin_only/', adminPageView, name='admin_only'),
    path('secure_data/', secureDataPageView, name='secure_data'),
]
