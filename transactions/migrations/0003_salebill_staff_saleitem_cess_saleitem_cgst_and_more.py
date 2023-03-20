# Generated by Django 4.1.7 on 2023-03-20 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("transactions", "0002_alter_purchasebill_supplier_delete_supplier"),
    ]

    operations = [
        migrations.AddField(
            model_name="salebill",
            name="staff",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staff",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="saleitem",
            name="cess",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="saleitem",
            name="cgst",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="saleitem",
            name="eway",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="saleitem",
            name="igst",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="saleitem",
            name="po",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="saleitem",
            name="sgst",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="saleitem",
            name="tcs",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="saleitem",
            name="total",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="saleitem",
            name="veh",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="saleitem",
            name="billno",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="saledetailsbillno",
                to="transactions.salebill",
            ),
        ),
        migrations.DeleteModel(
            name="SaleBillDetails",
        ),
    ]
