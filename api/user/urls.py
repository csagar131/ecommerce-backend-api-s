from django.urls import path
from .views import UserViewSet,signin,signout
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('login/', signin, name='signin'),
    path('logout/<int:id>/', signout, name='signin')
]

urlpatterns += router.urls