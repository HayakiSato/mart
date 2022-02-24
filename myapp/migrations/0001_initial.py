# Generated by Django 3.2.9 on 2021-12-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(default='', max_length=100)),
                ('pPrice', models.IntegerField(default=0)),
                ('pImages', models.CharField(default='', max_length=100)),
                ('pDescription', models.TextField(blank=True, default='')),
            ],
        ),
    ]
