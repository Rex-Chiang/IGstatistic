# Generated by Django 2.1.7 on 2019-04-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20190413_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Least_Commented_Posts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='Least_Liked_Posts',
            field=models.IntegerField(default=0),
        ),
    ]
