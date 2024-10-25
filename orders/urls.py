# orders/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register('', OrderViewSet, basename='order')

urlpatterns = router.urls