# Generated by Django 5.1.4 on 2024-12-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unis', '0003_remove_uni_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='uni',
            name='wage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
