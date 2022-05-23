from django.db import models

LICENCE_CHOICES = (
    ('b','B'),
    ('be', 'BE'),
    ('c','C'),
    ('ce','CE'),
    ('d','D'),
    ('de','DE'),
    ('e','E'),
)

class Rv(models.Model):
   vehicle = models.CharField(max_length=300)
   requiredLicence = models.CharField(max_length=6, choices=LICENCE_CHOICES, default='b')
   modelYear = models.IntegerField(default = 2020)
   maxPassangers = models.IntegerField(default = 5)
   beds = models.IntegerField(default = 0)
   otherInfo = models.TextField(default="")
   
   def __str__(self):
       return f"{self.vehicle} {self.modelYear}"
