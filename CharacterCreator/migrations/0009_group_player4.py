# Generated by Django 3.1.7 on 2021-03-25 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharacterCreator', '0008_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='player4',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
