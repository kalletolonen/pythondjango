from django.views.generic import ListView
from . import models

class AnimalListView(ListView): #inherits ListView
	model = models.Animal #in models.py

