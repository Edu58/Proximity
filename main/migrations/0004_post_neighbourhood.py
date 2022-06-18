# Generated by Django 4.0.5 on 2022-06-18 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood', to='main.neighbourhood'),
        ),
    ]
