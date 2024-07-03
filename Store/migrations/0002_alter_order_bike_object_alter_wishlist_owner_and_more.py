# Generated by Django 5.0.1 on 2024-05-14 06:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Bike_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bike', to='Store.bike'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wishlistitem',
            name='Cart_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishitem', to='Store.wishlist'),
        ),
    ]
