# Generated by Django 3.2.9 on 2021-11-23 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='aspect_ratio',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='tire',
            name='wheel_size',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='tire',
            name='width',
            field=models.CharField(max_length=4),
        ),
    ]