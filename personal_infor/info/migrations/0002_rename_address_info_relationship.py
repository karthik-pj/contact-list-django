# Generated by Django 4.1.7 on 2023-05-12 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="info",
            old_name="address",
            new_name="relationship",
        ),
    ]