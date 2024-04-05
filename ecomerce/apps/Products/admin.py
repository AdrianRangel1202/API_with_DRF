from django.contrib import admin
from apps.Products.models import MeasureUnit, Category, Indicador, Product

# Register your models here.
admin.site.register(MeasureUnit)
admin.site.register(Category)
admin.site.register(Indicador)
admin.site.register(Product)