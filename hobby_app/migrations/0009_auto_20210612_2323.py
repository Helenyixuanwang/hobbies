# Generated by Django 2.2 on 2021-06-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_app', '0008_auto_20210612_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='hobby_img',
            field=models.ImageField(default='default', upload_to='images/'),
        ),
    ]