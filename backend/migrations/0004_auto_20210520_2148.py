# Generated by Django 2.2.8 on 2021-05-20 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210520_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_type_of_product', models.CharField(default='Truck Logo', max_length=256)),
                ('single_image', models.ImageField(upload_to='uploads/products/single_images')),
                ('base_price', models.FloatField(default=0.0)),
                ('is_company_name_enable', models.BooleanField(default=False)),
                ('company_name_price', models.FloatField(default=0.0)),
                ('is_dot_number_enable', models.BooleanField(default=False)),
                ('dot_number_price', models.FloatField(default=0.0)),
                ('is_mc_number_enable', models.BooleanField(default=False)),
                ('mc_number_price', models.FloatField(default=0.0)),
                ('is_origin_enable', models.BooleanField(default=False)),
                ('origin_price', models.FloatField(default=0.0)),
                ('is_vim_number_enable', models.BooleanField(default=False)),
                ('vim_number_price', models.FloatField(default=0.0)),
                ('is_truck_number_enable', models.BooleanField(default=False)),
                ('truck_number_price', models.FloatField(default=0.0)),
                ('is_color_enable', models.BooleanField(default=False)),
                ('color_price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='base_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='company_name_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='display_in_prices',
        ),
        migrations.RemoveField(
            model_name='product',
            name='dot_number_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_color_enable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_company_name_enable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_dot_number_enable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_mc_number_enable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_origin_enable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_truck_number_enable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_vim_number_enable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mc_number_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='origin_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='truck_number_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vim_number_price',
        ),
        migrations.AlterField(
            model_name='product',
            name='type_of_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.ProductType'),
        ),
    ]