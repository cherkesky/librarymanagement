from django.db import models

class Library(models.Model):
  title = model.models.CharField(max_length=50)
  address = model.models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ("Library")
        verbose_name_plural = ("Librarys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Library_detail", kwargs={"pk": self.pk})
