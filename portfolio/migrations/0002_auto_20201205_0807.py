# Generated by Django 3.0.5 on 2020-12-05 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='liveLink',
            field=models.TextField(blank=True),
        ),
    ]
