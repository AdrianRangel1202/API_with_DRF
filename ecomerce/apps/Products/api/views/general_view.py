from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.Products.api.serializers.general_serializer import *
#from apps.Products.models import MeasureUnit




class MeasureUnitListAPIView(viewsets.GenericViewSet):
    serializer_class = MeasureUnitSerializer


    def get_queryset(self):
        return self.get_serializer().Meta.models.objects.all()


    """
    Retorna una lista de todas las unidades de medidas
    """

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response({data.data},status=status.HTTP_200_OK)

    
class CategoryListAPIView(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.models.objects.all()


    """
    Retorna una lista de todas las categorias
    """

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response({data.data},status=status.HTTP_200_OK)


class IndicadorListAPIView(viewsets.GenericViewSet):
    serializer_class = IndicadorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.models.objects.all()


    """
    Retorna una lista de todas los indicadores 
    """

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response({data.data},status=status.HTTP_200_OK)

    
