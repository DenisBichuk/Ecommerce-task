from rest_framework.serializers import ModelSerializer

from . import models
from users.serializers import UserSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title',)


class StockSerializer(ModelSerializer):
    class Meta:
        model = models.Stock
        fields = '__all__'


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = models.Equipment
        exclude = ('id', 'user', 'created_at', 'updated_at')

    def to_representation(self, instance):
        return EquipmentReadSerializer(
            context=self.context
        ).to_representation(instance=instance)


class EquipmentReadSerializer(ModelSerializer):
    category = CategorySerializer()
    user = UserSerializer()
    stock = StockSerializer()

    class Meta:
        model = models.Equipment
        fields = '__all__'
