from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    сooking_time = models.CharField(max_length=5, null=True, blank=True)


    def __str__(self):
        return self.name
