# Generated by Django 4.2.6 on 2023-11-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_team_pics"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(allow_unicode=True, default="default", unique=True),
        ),
    ]
