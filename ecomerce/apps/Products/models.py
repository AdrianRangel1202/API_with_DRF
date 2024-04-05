from django.db import models
from simple_history.models import HistoricalRecords
from apps.Base.models import BaseModel

# Create your models here.

class MeasureUnit(BaseModel):
    description = models.CharField('Descripcion', max_length= 50, blank= False, null = False, unique= True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidad de medidas'

    def __str__(self):
        return self.description


class Category(BaseModel):
    description = models.CharField('Descripcion', max_length= 50, blank= False, null = False, unique= True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.description
    


class Indicador(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default= 0)
    category_product = models.ForeignKey(Category, on_delete= models.CASCADE, verbose_name= 'Indicador de Ofertas')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicador de Ofertas'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        return f'Oferta de la Categoria {self.category_product}: {self.descount_value}%'
    

class Product(BaseModel):
    name = models.CharField('Nombre del Producto', max_length= 150, unique= True, blank= False, null= False)
    description = models.CharField('Descripcion de Productos', max_length= 200, blank= False, null = False)
    image = models.ImageField('Imagen del Productos', upload_to= 'products/', blank= True, null= True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, verbose_name= 'Categoria', null = True)
    Measue_unit = models.ForeignKey(MeasureUnit, on_delete= models.CASCADE, verbose_name= 'Unidad de Medida', null = True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name