from apps.Base.api import GeneralListAPIView
from apps.Products.api.serializers.general_serializer import *


class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer

    
class CategoryListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer


class IndicadorListAPIView(GeneralListAPIView):
    serializer_class = IndicadorSerializer

    
