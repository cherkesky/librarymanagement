from django.db import models
from .library import Library

class Book(models.Model):
  title = model.models.CharField(max_length=50)
  isbn = model.models.CharField(max_length=50)
  author = model.models.CharField(max_length=50)
  year = model.models.CharField(max_length=50)

  location = models.ForeignKey(Library, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
