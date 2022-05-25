## pw3 CRUD

I started @ 16.55.
  
The source for [the exercise](https://terokarvinen.com/2021/python-web-service-from-idea-to-production-2022/#pw3-crud)

The source for the code was our lecture on 2022/05/25 by [Tero Karvinen](https://terokarvinen.com).
  
**Hardware & Software**  
*Win 11 + VirtualBox 6.0 + Debian 11 Bullseye*  
  
*Hardware:*  
*CPU: AMD Ryzen 9 5900HS*  
*Mem: 16 Gt LPDDR4X*  
*Storage: 512 Gt M.2 2230 NVMe PCIe 3.0 SSD*  

# a) Vapaaehtoinen: CRUD. Tee alusta lähtien Django-ohjelma, jossa voit luoda (C), lukea (R), muokata (U) ja poistaa (D) tietueita. Keksi sille joku aihe, vaikka kalavale / tall tales. Tässä ohjelmassa ei tarvitse autentikoida käyttäjiä. Tästä tehtävästä ei tarvitse tehdä yksityiskohtaista raporttia, palauta ohjelman lähdekoodi, README.md ja ruutukaappaus. / Make a Django CRUD, return source code & README.

## The steps I took (just to keep a note for myself) for Django & Read:
1. Start a fresh VM
2. Update & Install bash-completion, micro and virtualenv
3. Created a folder, started a Django project, added a superuser, started a django app, ran migrations
4. Logged in to admin to check things out
5. Created a simple model with 1 field, registered that to admin.py and my app to settings.py
6. Made migrations and added some data
7. Made a modification to urls.py (a new path for reading all the objects)
8. Made a new view
9. Made a new folder for templates
10. Made a template, restarted the dev server
11. Updated my template to iterarate a list

(I tested at every step to make sure I was doing the right things.)

![pic 1. Read from database](/pics/pw3/1.png)  
*R was ½ done.*  

## View a single object (still R)

12. Added a new path to urls.py for my 2nd update-functionality (DetailView)
13. Added a class to views.py
14. Added a template

![pic 2. Read from database, single case](/pics/pw3/2.png)  
*R was done.*  

## Update an object

15. Updated my list template to have a link for each database object
16. Edited models to have a get_absolute_url -method
17. Added a link to the individual object from my list.html I forgot earlier
18. Added a link back to listing from detail.html
19. Added an update template

![pic 3. Update database](/pics/pw3/3.png)  
*U was done.*  

## Create an object

20. Updated my list template to have a "new" link
21. Updated urls.py
22. updated views.py

![pic 4. Create a new entry to  database](/pics/pw3/4.png)  
*C was done.*  

## Delete an object

23. Updated my list template to have a "delete" link for all items
24. Updated my urls.py
25. Update my views.py
26. Made a delete template

![pic 5. Delete an entry to database](/pics/pw3/5.png)  
*D was done.*  

Time was 17.55, so 1 hour from empty VM to working CRUD while taking these notes.

### Source code

## HTML

```Html
#rv_confirm_delete.html

<form method=post>
	{% csrf_token %}
	Are you sure you wish to delete "{{ object }}"<br>
	<input type=submit value=Delete>
<form>
```

```Html
#rv_detail.html

<h1>Hello single</h1>

<p>
	Name: {{ object.name }}<br>
	Manufactuer: {{ object.manufacturer }}<br>
	<a href="/">Back to start</a>
</p>
```

```Html
#rv_form.html

<form method=post>{% csrf_token %}
	{{ form.as_p }}
	<input type="submit">
</form>
```

```Html
#rv_list.html

<h1>Rv list</h1>

{% for rv in  object_list %}
	<p>
		<a href="{{ rv.get_absolute_url }}">{{ rv.name }}</a> <br>
		{{ rv.manufacturer}}<br>
		<a href="{{ rv.get_absolute_url }}/update">Update</a> - 
		<a href="{{ rv.get_absolute_url }}/delete">Delete</a>
	</p>
{% endfor %}

<a href="/new">New</a>
```

##PYTHON

```Python
#models.py

from django.db import models

class Rv(models.Model):
    name = models.CharField(max_length=300)
    manufacturer = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.manufacturer}"

    def get_absolute_url(self):
        return f"/rv/{self.pk}"
```

```Python
#views.py

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

class RvListView(ListView): 
	model = models.Rv 

class RvDetailView(DetailView):
	model = models.Rv 

class RvUpdateView(UpdateView): 
	model = models.Rv 
	fields = "__all__"
	success_url = "/"

class RvCreateView(CreateView): 
	model = models.Rv 
	fields = "__all__"
	success_url = "/"

class RvDeleteView(DeleteView): 
	model = models.Rv
	success_url = "/"
```

```Admin.py
from django.contrib import admin
from . import models

admin.site.register(models.Rv)
```

```Python
#urls.py

from django.contrib import admin
from django.urls import path
from rentrv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.RvListView.as_view()),
    path('rv/<int:pk>', views.RvDetailView.as_view()),
    path('rv/<int:pk>/update', views.RvUpdateView.as_view()),
    path('new/', views.RvCreateView.as_view()),
    path('rv/<int:pk>/delete', views.RvDeleteView.as_view()),
]
```

```Python
#settings.py (not complete)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rentrv', #Added this
]
```
