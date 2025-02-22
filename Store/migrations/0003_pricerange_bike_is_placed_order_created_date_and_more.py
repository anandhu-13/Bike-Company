# Generated by Django 5.0.1 on 2024-05-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_alter_order_bike_object_alter_wishlist_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='is_placed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('cod', 'cod'), ('online', 'online')], default='cod', max_length=200),
        ),
    ]
