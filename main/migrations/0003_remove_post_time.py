# Generated by Django 4.0.5 on 2022-06-18 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_post_neighbourhood_business_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
    ]
