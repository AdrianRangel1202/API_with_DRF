from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.Products.api.serializers.general_serializer import *
#from apps.Products.models import MeasureUnit




class MeasureUnitListAPIView(viewsets.GenericViewSet):
    serializer_class = MeasureUnitSerializer


    def get_queryset(self):
        return self.get_serializer().Meta.models.objects.all()


    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response({data.data},status=status.HTTP_200_OK)






    
class CategoryListAPIView(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer

    # Busca TODOS los objetos que esten en categorias con el estado en verdadero
    def get_queryset(self):
        return self.get_serializer().Meta.models.objects.filter(state = True)

    # Busca y filtra una categoria que coincida con el id = pk que se le envie y que tenga su estado en verdadero
    def get_object(self):
        return self.get_serializer().Meta.models.objects.filter(id = self.kwargs['pk'], state = True)

 
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response({data.data},status=status.HTTP_200_OK)


    def create(self, request):
        serializers = self.serializer_class(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'Categoria creada con exito!.'},status=status.HTTP_201_CREATED)
        return Response({'Error': serializers.errors},status= status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        if self.get_object.exists():
            serializers = self.serializer_class(instance = self.get_object().get(), data = request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({'message':'Categoria Actualizada con exito!.'},status=status.HTTP_200_OK)
            return Response({'Error': serializers.errors},status= status.HTTP_400_BAD_REQUEST)



class IndicadorListAPIView(viewsets.GenericViewSet):
    serializer_class = IndicadorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.models.objects.all()


    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response({data.data},status=status.HTTP_200_OK)

    
