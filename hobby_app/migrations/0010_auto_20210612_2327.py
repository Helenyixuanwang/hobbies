# Generated by Django 2.2 on 2021-06-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_app', '0009_auto_20210612_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='hobby_img',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
