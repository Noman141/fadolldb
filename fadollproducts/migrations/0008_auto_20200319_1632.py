# Generated by Django 3.0 on 2020-03-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fadollproducts', '0007_auto_20200319_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='CreatedDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='ModifiedDate',
            field=models.DateTimeField(),
        ),
    ]
