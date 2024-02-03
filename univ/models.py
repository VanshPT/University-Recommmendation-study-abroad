from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    global_ranking = models.IntegerField()

    def __str__(self):
        return self.name
