# Generated by Django 2.1.1 on 2020-02-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_prbac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='deny',
            field=models.BooleanField(default=False),
        ),
    ]
