# Generated by Django 5.0.6 on 2024-06-02 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_rename_usercommentform_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='time',
        ),
    ]
