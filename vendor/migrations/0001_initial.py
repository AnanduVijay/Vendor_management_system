# Generated by Django 5.0 on 2023-12-19 16:32

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vendor",
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
                ("name", models.CharField(max_length=130)),
                ("contact_details", models.TextField(max_length=200)),
                ("adress", models.CharField(max_length=200)),
                (
                    "vendor_code",
                    models.CharField(
                        default=uuid.uuid4, editable=False, max_length=4, unique=True
                    ),
                ),
                ("on_time_delivery_rate", models.FloatField(blank=True, null=True)),
                ("quality_rating_avg", models.FloatField(blank=True, null=True)),
                ("average_response_time", models.FloatField(blank=True, null=True)),
                ("fulfillment_rate", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
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
                (
                    "po_number",
                    models.CharField(
                        default=uuid.uuid4, editable=False, max_length=4, unique=True
                    ),
                ),
                ("order_date", models.DateTimeField(null=True)),
                ("delivery_date", models.DateTimeField(null=True)),
                ("items", models.JSONField()),
                ("quantity", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("completed", "Completed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="pending",
                        max_length=50,
                    ),
                ),
                ("quality_rating", models.FloatField(null=True)),
                ("issue_date", models.DateTimeField(null=True)),
                ("acknowledgment_date", models.DateTimeField(null=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="vendor.vendor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Performance",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                ("on_time_delivery_rate", models.FloatField(blank=True, null=True)),
                ("quality_rating_avg", models.FloatField(blank=True, null=True)),
                ("average_response_time", models.FloatField(blank=True, null=True)),
                ("fulfillment_rate", models.FloatField(blank=True, null=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="vendor.vendor"
                    ),
                ),
            ],
        ),
    ]
