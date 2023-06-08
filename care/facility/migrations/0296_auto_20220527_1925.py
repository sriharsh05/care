# Generated by Django 2.2.11 on 2022-05-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0295_merge_20220527_1430"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="facilitycapacity",
            options={"verbose_name_plural": "Facility Capacities"},
        ),
        migrations.AlterField(
            model_name="asset",
            name="asset_class",
            field=models.CharField(
                blank=True,
                choices=[("ONVIF", "onvif"), ("HL7MONITOR", "hl7monitor")],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
    ]
