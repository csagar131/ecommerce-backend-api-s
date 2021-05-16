from django.urls import path
from .views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = router.urls

