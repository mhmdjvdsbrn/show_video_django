# Generated by Django 4.0.4 on 2022-05-23 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_delete_videoproxy_videoallproxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='publish_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Published'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]
