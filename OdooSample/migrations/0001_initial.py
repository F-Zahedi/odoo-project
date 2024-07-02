# Generated by Django 5.0.6 on 2024-07-01 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("Name", models.CharField(max_length=250)),
                ("Details", models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("FirstName", models.CharField(max_length=100)),
                ("LastName", models.CharField(max_length=100)),
                ("PhoneNumber", models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name="Deliver",
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
                ("Name", models.CharField(max_length=100)),
                ("ContactNumber", models.CharField(max_length=11)),
                ("DeliverType", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("FirstName", models.CharField(max_length=100)),
                ("LastName", models.CharField(max_length=100)),
                ("PhoneNumber", models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
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
                ("Name", models.CharField(max_length=250)),
                ("Country", models.CharField(max_length=250)),
                ("ContactNumber", models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                    "CustomerId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="OdooSample.customer",
                    ),
                ),
                (
                    "DeliveryTypeId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="OdooSample.deliver",
                    ),
                ),
                (
                    "EmployeeId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="OdooSample.employee",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("Name", models.CharField(max_length=250)),
                ("FeePrice", models.PositiveBigIntegerField()),
                (
                    "CategoryId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="OdooSample.category",
                    ),
                ),
                (
                    "SupplierId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="OdooSample.supplier",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderDetail",
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
                ("Count", models.PositiveBigIntegerField()),
                ("FeePrice", models.PositiveBigIntegerField()),
                (
                    "OrderId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="OdooSample.order",
                    ),
                ),
                (
                    "ProductId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="OdooSample.product",
                    ),
                ),
            ],
        ),
    ]
