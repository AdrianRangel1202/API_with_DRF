from apps.Products.models import MeasureUnit, Category, Indicador
from rest_framework import serializers


class MeasureUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeasureUnit
        exclude = ('state','created_date','modified_date','deleted_date')


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('state','created_date','modified_date','deleted_date')



class IndicadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicador
        exclude = ('state','created_date','modified_date','deleted_date')   