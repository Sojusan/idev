"""Test models."""
from django.db import models


class Book(models.Model):
    """Test model."""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

    class Meta:
        """Meta class for Book model."""
        verbose_name = "Book"
        verbose_name_plural = "Books"
