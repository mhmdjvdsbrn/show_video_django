# Generated by Django 4.0.5 on 2022-06-17 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0018_alter_playlistrelated_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlistrelated',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
