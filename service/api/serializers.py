from rest_framework import serializers
from service.models import Category, Maintenance, Recomendation


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    category = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    price = serializers.CharField(required=True)

    class Meta:
        model = Maintenance
        fields = '__all__'


class RecSerializer(serializers.ModelSerializer):
    marka = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    year = serializers.CharField(required=True)
    mileage = serializers.CharField(required=True)
    maintenance = serializers.CharField(required=True)


    class Meta:
        model = Recomendation
        fields = '__all__'