from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import home
from .category.views import CategoryViewSet



urlpatterns = [
   path('user/', include('api.user.urls')),
   path('category/', include('api.category.urls')),
   path('product/', include('api.product.urls')),
   path('', home, name = 'api.home'),
]
