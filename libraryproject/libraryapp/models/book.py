from django.db import models

class Book(models.Model):
  title = model.models.CharField(max_length=50)
  isbn = model.models.CharField(max_length=50)
  author = model.models.CharField(max_length=50)
  year = model.models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
