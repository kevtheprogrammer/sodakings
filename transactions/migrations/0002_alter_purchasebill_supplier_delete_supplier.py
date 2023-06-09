# Generated by Django 4.1.7 on 2023-03-20 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchasebill",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="supplier",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Supplier",
        ),
    ]
