# Generated by Django 3.2 on 2021-04-16 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launch', '0004_announcement_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='name',
            new_name='customer',
        ),
    ]
