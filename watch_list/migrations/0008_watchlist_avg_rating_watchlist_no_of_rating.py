# Generated by Django 4.2.1 on 2023-05-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_list', '0007_alter_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='no_of_rating',
            field=models.IntegerField(default=0),
        ),
    ]