from django.contrib import admin
from django.urls import path
from adoptme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AnimalListView.as_view()),
]
