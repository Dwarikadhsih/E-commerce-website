# Generated by Django 3.2.4 on 2021-12-14 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_orderupdate_phone_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderupdate",
            name="Phone_number",
        ),
    ]