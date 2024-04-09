from django.contrib import admin
from apps.Products.models import MeasureUnit, Category, Indicador, Product


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


# Register your models here.
admin.site.register(MeasureUnit,MeasureUnitAdmin)
admin.site.register(Category, categoryAdmin)
admin.site.register(Indicador)
admin.site.register(Product)