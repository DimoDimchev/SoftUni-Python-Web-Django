# Generated by Django 3.2.2 on 2021-05-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates_advanced', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]