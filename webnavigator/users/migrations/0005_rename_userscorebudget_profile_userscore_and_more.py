# Generated by Django 5.1.4 on 2024-12-27 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_subjects_remove_profile_bio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='userScoreBudget',
            new_name='userScore',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='userScorePaid',
        ),
    ]