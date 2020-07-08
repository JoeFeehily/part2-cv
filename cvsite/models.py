from django.conf import settings
from django.db import models


class Section(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.id = id #needed?
        self.save()

    def __str__(self):
        return self.title