# Generated by Django 3.1.7 on 2021-03-31 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharacterCreator', '0013_spells'),
    ]

    operations = [
        migrations.AddField(
            model_name='spells',
            name='concentration',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spells',
            name='materialComponents',
            field=models.CharField(default='No components required.', max_length=200),
            preserve_default=False,
        ),
    ]
