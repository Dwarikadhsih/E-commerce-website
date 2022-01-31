# Generated by Django 3.2.4 on 2021-12-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="productdetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(max_length=100)),
                ("heading0", models.CharField(max_length=10000)),
                ("heading1", models.CharField(default="", max_length=50)),
                ("heading2", models.CharField(default="", max_length=50)),
                ("product_date", models.DateField()),
                ("image", models.ImageField(default="", upload_to="Shops/images")),
            ],
        ),
    ]
