# Generated by Django 3.1.7 on 2021-03-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_remove_tweetdata_friend_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetdata',
            name='profile_image_url',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='tweetdata',
            name='user_name',
            field=models.TextField(default=999),
            preserve_default=False,
        ),
    ]
