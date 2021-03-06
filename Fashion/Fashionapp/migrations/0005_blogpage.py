# Generated by Django 3.0.7 on 2020-08-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fashionapp', '0004_auto_20200816_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='pics')),
                ('date', models.DateTimeField(default='')),
                ('description', models.TextField(default='', max_length=200)),
            ],
        ),
    ]
