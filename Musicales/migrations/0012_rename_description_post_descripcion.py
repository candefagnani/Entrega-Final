# Generated by Django 4.1.7 on 2023-04-14 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musicales', '0011_rename_leading_actor_post_actor_principal_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='descripcion',
        ),
    ]