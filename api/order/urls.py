from django.urls import path, include
from .views import OrderViewSet,add_order
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', OrderViewSet)

urlpatterns = [
    path('add/<str:id>/<str:token>/',add_order,name='add_order')
]

urlpatterns += router.urls