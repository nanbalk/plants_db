from django.db import models

# Create your models here.

class Plants(models.Model):
    name = models.CharField(max_length=200, null=True)
    bioactive_compound = models.CharField(max_length=200, null=True)
    uses = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name