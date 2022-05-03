# Generated by Django 3.1.7 on 2021-04-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210415_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('abs', models.CharField(max_length=256)),
                ('kws', models.CharField(max_length=128)),
                ('date', models.CharField(max_length=32)),
                ('userid', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=99999)),
                ('type', models.CharField(max_length=32)),
            ],
        ),
    ]
