# Generated by Django 5.0.6 on 2024-06-02 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_remove_comment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='lastname',
        ),
    ]
