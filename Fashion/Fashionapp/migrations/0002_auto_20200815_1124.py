# Generated by Django 3.0.7 on 2020-08-15 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fashionapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='Image',
            field=models.ImageField(default='SOME STRING', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='Percentag',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='offers',
            name='Price',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='offers',
            name='Service',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
