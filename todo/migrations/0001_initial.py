# Generated by Django 3.1.6 on 2021-03-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TweetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenname', models.CharField(max_length=150)),
                ('tweetid', models.IntegerField()),
                ('postdate', models.DateTimeField()),
                ('body', models.TextField()),
                ('rt', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('url', models.URLField()),
            ],
        ),
    ]