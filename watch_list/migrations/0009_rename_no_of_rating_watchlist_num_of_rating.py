# Generated by Django 4.2.1 on 2023-05-16 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch_list', '0008_watchlist_avg_rating_watchlist_no_of_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='no_of_rating',
            new_name='num_of_rating',
        ),
    ]
