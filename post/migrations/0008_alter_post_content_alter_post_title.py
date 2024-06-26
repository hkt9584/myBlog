# Generated by Django 5.0.3 on 2024-05-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0007_alter_post_content_alter_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.CharField(max_length=300, verbose_name="內容"),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=20, verbose_name="標題"),
        ),
    ]
