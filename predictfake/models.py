from django.db import models

# Create your models here.
class News(models.Model):
    keywords = models.CharField(max_length=400, blank=True)
    lang = models.CharField(max_length=5, blank=True)
    country = models.CharField(max_length=15, blank=True)
    date = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return "news " + str(self.id)