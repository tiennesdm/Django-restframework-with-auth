from django.db import models

# Create your models here.
class CrudRestApi(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.name


