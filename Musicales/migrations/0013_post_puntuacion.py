# Generated by Django 4.1.7 on 2023-04-21 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicales', '0012_rename_description_post_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='puntuacion',
            field=models.IntegerField(blank=True, choices=[(1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')], null=True),
        ),
    ]