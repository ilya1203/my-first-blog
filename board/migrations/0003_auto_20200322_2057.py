# Generated by Django 3.0.2 on 2020-03-22 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200322_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccont',
            name='video',
            field=models.TextField(blank=True, null=True),
        ),
    ]
