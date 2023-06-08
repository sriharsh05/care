# Generated by Django 2.2.11 on 2022-08-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0308_auto_20220805_2247"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="last_serviced_on",
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="asset",
            name="manufacturer",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name="asset",
            name="notes",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AddField(
            model_name="asset",
            name="warranty_amc_end_of_validity",
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
