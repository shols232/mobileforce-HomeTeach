# Generated by Django 3.0.8 on 2020-07-15 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confirmation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_date',
        ),
    ]