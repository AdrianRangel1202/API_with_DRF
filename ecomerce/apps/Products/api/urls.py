from django.urls import path
from apps.Products.api.views.general_view import MeasureUnitListAPIView, CategoryListAPIView, IndicadorListAPIView

urlpatterns = [
    #URL General_view
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name= 'Unidades De Medida'),
    path('category/', CategoryListAPIView.as_view(), name= 'Categoria de Productos'),
    path('indicator/', IndicadorListAPIView.as_view(), name= 'Indicador de Ofertas'), 
]