# Generated by Django 4.2.6 on 2023-11-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_team_post_category_post_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="pics",
            field=models.ImageField(default="default", upload_to=""),
        ),
    ]
