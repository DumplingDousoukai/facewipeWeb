# Generated by Django 3.1.7 on 2021-04-09 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20210318_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendfriendid',
            name='friend_friend_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='friendid',
            name='friend_id',
            field=models.TextField(),
        ),
    ]
