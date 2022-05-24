from django.db import models

class Animal(models.Model):
    animal = models.CharField(max_length=300)
    name = models.CharField(max_length=300, default="Keijo")
      
    def __str__(self):
        return f"{self.animal}"
