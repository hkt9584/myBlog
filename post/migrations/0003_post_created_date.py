# Generated by Django 5.0.3 on 2024-04-17 14:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0002_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
