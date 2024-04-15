from rest_framework.routers import DefaultRouter
from apps.Products.api.views.product_view import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='Products')

urlpatterns = router.urls