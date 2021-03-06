# Generated by Django 3.1.7 on 2021-04-09 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FriendFriendID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_friend_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FriendID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TweetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image_url', models.TextField()),
                ('user_name', models.TextField()),
            ],
        ),
    ]
