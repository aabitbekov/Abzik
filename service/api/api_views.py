from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from service.api.serializers import CategorySerializer, MaintenanceSerializer, RecSerializer
from service.models import Category, Maintenance, Recomendation


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveAPIView(RetrieveAPIView, RetrieveUpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'


class MaintenanceListAPIView(ListAPIView):
    serializer_class = MaintenanceSerializer
    queryset = Maintenance.objects.all()


class MaintenanceRetrieveAPIView(RetrieveAPIView):
    serializer_class = MaintenanceSerializer
    queryset = Maintenance.objects.all()
    lookup_field = 'id'


class RecListAPIView(ListAPIView):
    serializer_class = RecSerializer
    queryset = Recomendation.objects.all()


class RecByMarkaListAPIView(ListAPIView):
    serializer_class = RecSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Recomendation.objects.all()
    filterset_fields = ['marka', 'model', 'year']

