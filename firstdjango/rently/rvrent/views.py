from django.views.generic import ListView #class based generic view
from . import models

class RvListView(ListView): #inherits ListView
	model = models.Rv #in models.py
