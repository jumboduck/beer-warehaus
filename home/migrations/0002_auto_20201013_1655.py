# Generated by Django 3.1.2 on 2020-10-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='cta_link',
            field=models.URLField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='slide',
            name='cta_txt',
            field=models.CharField(max_length=30),
        ),
    ]
