"""Initial data with Books."""
# Generated by Django 5.0.1 on 2024-01-25 06:58

import time

from django.apps.registry import Apps
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

from idev.models import Book


def load_initial_data(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    """Load initial data."""
    book_model: Book = apps.get_model("idev", "Book")

    start = time.perf_counter_ns()

    for index in range(10_000):
        book_model.objects.create(
            title=f"Title {index}",
            author=f"Author {index}",
        )

    print(f'\033[92m Load time: {(time.perf_counter_ns() - start) / 1_000_000_000} seconds. \033[0m')

def reverse_code(apps: Apps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    """Remove initial data."""
    book_model: Book = apps.get_model("idev", "Book")
    book_model.objects.all().delete()


class Migration(migrations.Migration):
    """Long running initial data."""

    dependencies = [
        ('idev', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(code=load_initial_data, reverse_code=reverse_code)
    ]
