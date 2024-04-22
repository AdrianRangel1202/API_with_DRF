from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import viewsets
from apps.Base.api import GeneralListAPIView
from apps.Products.api.serializers.product_serializer import ProductSerializer
from apps.users.authentication_mixing import Authentication



class ProductViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ProductSerializer


    def get_queryset(self, pk = None):
        if pk == None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    #Muestra la lista de todos los productos en un estado True 
    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto Creado Con Exito'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = self.serializer_class(product, data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status= status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def destroy(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto Eliminado Correctamente!'}, status = status.HTTP_200_OK)
        return Response({'message':'Producto No Encontrado'}, status=status.HTTP_400_BAD_REQUEST)


