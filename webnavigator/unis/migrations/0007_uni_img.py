# Generated by Django 5.1.4 on 2024-12-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unis', '0006_rename_data_uni_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='uni',
            name='img',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]