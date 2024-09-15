# Generated by Django 5.1.1 on 2024-09-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExtractedData",
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
                ("username", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("pdf_file", models.FileField(upload_to="pdfs/")),
                ("nouns", models.TextField()),
                ("verbs", models.TextField()),
            ],
        ),
    ]
