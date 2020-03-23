# Generated by Django 3.0 on 2019-12-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fadollproducts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributevalues',
            name='logo',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='categories',
            name='logo',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customerclasses',
            name='logo',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='departments',
            name='logo',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='LargeImage',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='SmallImage',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productnatures',
            name='logo',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='products',
            name='ProductImage',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='logo',
            field=models.TextField(max_length=255),
        ),
    ]
