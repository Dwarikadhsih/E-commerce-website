# Generated by Django 3.2.4 on 2021-12-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_alter_orders_item_json"),
    ]

    operations = [
        migrations.CreateModel(
            name="Solution",
            fields=[
                ("S_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("desc", models.CharField(max_length=1000)),
                ("soultion", models.CharField(max_length=10000)),
            ],
        ),
    ]
