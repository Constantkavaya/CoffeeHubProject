# Generated by Django 3.2.8 on 2021-11-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='uploads/products/'),
            preserve_default=False,
        ),
    ]
