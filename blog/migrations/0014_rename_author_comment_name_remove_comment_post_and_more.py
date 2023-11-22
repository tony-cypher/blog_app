# Generated by Django 4.2.6 on 2023-11-22 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0013_contact"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="author",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="post",
        ),
        migrations.AddField(
            model_name="comment",
            name="email",
            field=models.EmailField(default="default", max_length=254),
        ),
        migrations.AddField(
            model_name="post",
            name="comments",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_comments",
                to="blog.comment",
            ),
        ),
    ]
