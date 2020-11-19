# Generated by Django 3.1.2 on 2020-11-19 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producers', '0001_initial'),
        ('products', '0009_auto_20201031_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='producers.producer'),
        ),
    ]
