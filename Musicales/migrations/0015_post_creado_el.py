# Generated by Django 4.1.7 on 2023-04-21 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Musicales', '0014_alter_post_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='creado_el',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]