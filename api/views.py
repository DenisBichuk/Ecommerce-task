from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from . import models, serializers, permissions


class ProtectedViewSet(ModelViewSet):
    permission_classes = (
        permissions.IsAdminOrReadOnly,
    )
    pagination_class = LimitOffsetPagination


class CategoryViewSet(ProtectedViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class EquipmentViewSet(ProtectedViewSet):
    queryset = models.Equipment.objects.select_related(
        'category',
        'stock',
        'user'
    )
    serializer_class = serializers.EquipmentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StockViewSet(ProtectedViewSet):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer
