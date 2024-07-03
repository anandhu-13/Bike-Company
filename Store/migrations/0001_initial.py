# Generated by Django 5.0.1 on 2024-03-13 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='bike_images')),
                ('Model_year', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('km', models.PositiveBigIntegerField()),
                ('category_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='Store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=200, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('total', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('order-placed', 'order-placed'), ('intransit', 'intransit'), ('dispatched', 'dispatched'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='order-placed', max_length=200)),
                ('Bike_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.bike')),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
                ('serviced', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=200)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='repair', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_order_placed', models.BooleanField(default=False)),
                ('Bike_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.bike')),
                ('Cart_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitem', to='Store.wishlist')),
            ],
        ),
    ]
