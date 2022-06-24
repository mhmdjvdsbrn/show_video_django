# Generated by Django 4.0.4 on 2022-05-21 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_videopublishedproxy_alter_videoproxy_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VideoProxy',
        ),
        migrations.CreateModel(
            name='VideoAllProxy',
            fields=[
            ],
            options={
                'verbose_name': 'All video',
                'verbose_name_plural': 'All videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]