# Generated by Django 4.1.7 on 2023-04-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicales', '0008_alter_profile_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(default='default.png', upload_to='profiles'),
        ),
    ]
