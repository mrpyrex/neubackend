from django.db import models
from django.utils import timezone

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=250)
    desciption = models.TextField()
    thumb = models.URLField()
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=250)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
