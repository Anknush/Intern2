# Generated by Django 3.0.7 on 2020-08-15 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service', models.CharField(max_length=100)),
                ('Percentag', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
            ],
        ),
    ]