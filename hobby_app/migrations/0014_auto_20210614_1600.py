# Generated by Django 2.2 on 2021-06-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby_app', '0013_auto_20210613_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='liked_hobbies', to='hobby_app.User'),
        ),
    ]
