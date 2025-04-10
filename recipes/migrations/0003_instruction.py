# Generated by Django 5.1.7 on 2025-04-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_remove_ingredient_description_recipe_favorites_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Instruction",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="instructions/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
