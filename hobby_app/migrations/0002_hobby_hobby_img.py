# Generated by Django 2.2 on 2021-06-07 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='hobby_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]