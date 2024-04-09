from django.urls import path
from apps.Products.api.views.general_view import MeasureUnitListAPIView, CategoryListAPIView, IndicadorListAPIView
from apps.Products.api.views.product_view import (
    ProductListAPIView, 
    ProductoCreateAPIView,
    ProductRetriveAPIView,
    ProductoDestroyAPIView,
)
urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name= 'Unidades De Medida'),
    path('category/', CategoryListAPIView.as_view(), name= 'Categoria de Productos'),
    path('indicator/', IndicadorListAPIView.as_view(), name= 'Indicador de Ofertas'),
    path('products/list', ProductListAPIView.as_view(), name= 'Lista de Productos'),
    path('products/create', ProductoCreateAPIView.as_view(), name= 'Crear Productos'),
    path('products/filter/<int:pk>', ProductRetriveAPIView.as_view(), name= 'Filtrar Productos'),
    path('products/destroy/<int:pk>', ProductoDestroyAPIView.as_view(), name= 'Eliminar Productos'),
]