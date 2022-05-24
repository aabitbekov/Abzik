from django.urls import path

from service.api.api_views import CategoryListAPIView, CategoryRetrieveAPIView, MaintenanceListAPIView, \
    MaintenanceRetrieveAPIView, RecListAPIView, RecByMarkaListAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(),name='categories'),
    path('categories/<str:id>',CategoryRetrieveAPIView.as_view(),name='categories_id'),
    path('maintenance/', MaintenanceListAPIView.as_view(), name='maintenance'),
    path('maintenance/<str:id>', MaintenanceRetrieveAPIView.as_view(), name='maintenance_category'),
    path('rec/', RecListAPIView.as_view(), name='rec'),
    path('rec/find/', RecByMarkaListAPIView.as_view())
]