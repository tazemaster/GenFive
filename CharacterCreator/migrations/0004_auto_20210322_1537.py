# Generated by Django 3.1.7 on 2021-03-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharacterCreator', '0003_user_race'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='race',
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(default='NULL', max_length=25),
            preserve_default=False,
        ),
    ]
