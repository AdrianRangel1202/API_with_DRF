from rest_framework.routers import DefaultRouter
from apps.Products.api.views.product_view import ProductViewSet
from apps.Products.api.views.general_view import MeasureUnitListAPIView, CategoryListAPIView, IndicadorListAPIView



router = DefaultRouter()
router.register(r'', ProductViewSet, basename='Products')
router.register(r'measure-unit', MeasureUnitListAPIView, basename='Measure_unit')
router.register(r'category', CategoryListAPIView, basename='Category')
router.register(r'indicator', IndicadorListAPIView, basename='Indicator')

urlpatterns = router.urls