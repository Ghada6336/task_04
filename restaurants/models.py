from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.DateTimeField(auto_now_add=True)
    closing_time = models.CharField(max_length=120)

    def __str__(self):
        return self.name
