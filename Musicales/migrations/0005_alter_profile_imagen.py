# Generated by Django 4.1.7 on 2023-04-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicales', '0004_alter_profile_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(default='https://us.123rf.com/450wm/balabolka/balabolka2102/balabolka210200154/164287712-ilustraci%C3%B3n-de-garabato-de-dibujos-animados-dibujados-a-mano-de-nueva-york-dise%C3%B1o-divertido-de-la.jpg?ver=6.jpg', upload_to=''),
        ),
    ]
