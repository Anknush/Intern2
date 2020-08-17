# Generated by Django 3.0.7 on 2020-08-16 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fashionapp', '0002_auto_20200815_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default=' ', max_length=100)),
                ('image', models.ImageField(default=' ', upload_to='pics')),
                ('text', models.TextField(default=' ', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='offers',
            name='Image',
            field=models.ImageField(default=' ', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='Percentag',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='offers',
            name='Price',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='offers',
            name='Service',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
