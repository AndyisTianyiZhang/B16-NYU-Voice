# Generated by Django 4.2 on 2023-05-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NYUVoiceapp', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Student',
            field=models.BooleanField(default=True),
        ),
    ]
