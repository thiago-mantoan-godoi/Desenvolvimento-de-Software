# Generated by Django 3.1.2 on 2020-11-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=200),
            preserve_default=False,
        ),
    ]
