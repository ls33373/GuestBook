# Generated by Django 5.1.2 on 2024-11-09 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0003_rename_passward_guestbook_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestbook',
            name='password',
        ),
    ]