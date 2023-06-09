# Generated by Django 4.2 on 2023-04-14 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='название')),
                ('is_publish', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='название')),
            ],
            options={
                'verbose_name': 'topping',
                'verbose_name_plural': 'toppings',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='цена')),
                ('is_special', models.BooleanField(default=False)),
                ('is_vegan', models.BooleanField(default=False)),
                ('is_publish', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='food', to='menu.categoryfood', verbose_name='категория')),
                ('topping', models.ManyToManyField(related_name='food', to='menu.topping', verbose_name='ингредиенты')),
            ],
            options={
                'verbose_name': 'food',
                'verbose_name_plural': 'foods',
            },
        ),
    ]
