# Generated by Django 3.1.7 on 2021-04-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210416_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='abs',
        ),
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='kws',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.RemoveField(
            model_name='article',
            name='type',
        ),
        migrations.RemoveField(
            model_name='article',
            name='userid',
        ),
    ]
