# Generated by Django 4.0.5 on 2022-06-20 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_neighbourhood_admin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='neighbourhood',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
