# Generated by Django 3.0.2 on 2020-04-04 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_ccont_textcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccont',
            name='photo',
            field=models.TextField(blank=True, null=True),
        ),
    ]