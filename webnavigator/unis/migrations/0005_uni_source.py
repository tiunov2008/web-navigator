# Generated by Django 5.1.4 on 2024-12-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unis', '0004_uni_wage'),
    ]

    operations = [
        migrations.AddField(
            model_name='uni',
            name='source',
            field=models.URLField(null=True),
        ),
    ]