# Generated by Django 5.1.2 on 2024-11-09 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbook',
            name='passward',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
