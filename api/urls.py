from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'categories', viewset=views.CategoryViewSet)
router.register(r'equipment', viewset=views.EquipmentViewSet)
router.register(r'stocks', viewset=views.StockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
