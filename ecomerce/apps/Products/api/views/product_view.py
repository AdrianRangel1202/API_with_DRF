from rest_framework.response import Response
from rest_framework import generics, status
from apps.Base.api import GeneralListAPIView
from apps.Products.api.serializers.product_serializer import ProductSerializer


class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer


class ProductoCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto Creado Con Exito'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ProductRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

class ProductoDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def delete(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto Eliminado Correctamente!'}, status = status.HTTP_200_OK)
        return Response({'message':'Producto No Encontrado'}, status=status.HTTP_400_BAD_REQUEST)