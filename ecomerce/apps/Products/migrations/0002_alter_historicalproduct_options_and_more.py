# Generated by Django 5.0.3 on 2024-04-05 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalproduct',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Producto', 'verbose_name_plural': 'historical Productos'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='measure_unit',
        ),
        migrations.RemoveField(
            model_name='historicalcategory',
            name='measure_unit',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='Measue_unit',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Products.measureunit', verbose_name='Unidad de Medida'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='category',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Products.category', verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='product',
            name='Measue_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.measureunit', verbose_name='Unidad de Medida'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.category', verbose_name='Categoria'),
        ),
    ]
