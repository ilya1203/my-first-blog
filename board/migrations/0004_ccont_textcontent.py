# Generated by Django 3.0.2 on 2020-03-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200322_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccont',
            name='textContent',
            field=models.TextField(blank=True, null=True),
        ),
    ]
