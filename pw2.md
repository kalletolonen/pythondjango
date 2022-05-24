## pw2 ListView

I started @ 16.55.
  
The source for [the exercise](https://terokarvinen.com/2021/python-web-service-from-idea-to-production-2022/#pw2-listview)
  
**Hardware & Software**  
*Win 11 + VirtualBox 6.0 + Debian 11 Bullseye*  
  
*Hardware:*  
*CPU: AMD Ryzen 9 5900HS*  
*Mem: 16 Gt LPDDR4X*  
*Storage: 512 Gt M.2 2230 NVMe PCIe 3.0 SSD*  

### a) Tee alusta lähtien uusi Django-projekti. Tee siihen sivu, joka listaa tietueita tietokannasta ilman kirjautumista. Valitse jokin muu aihe kuin aiemman esimerkin CRM. Aivan simppeli esimerkkiprojekti riittää, mutta valitse sille jokin esimerkkiaihe. / Make a brand new Django project that has a view that lists objects from a database

A good tutorial for the first part can be found here: https://terokarvinen.com/2022/django-instant-crm-tutorial/

I will only list the commands for setting up a dev environment. You can find a more complete explanation of the process on my [previous article](https://github.com/kalletolonen/pythondjango/blob/main/pw1.md). 

The project is about creating an art database.
	
	cd
	sudo apt-get update && sudo apt-get install -y virtualenv
	mkdir collectorshaven
	cd collectorshaven/
	virtualenv --system-site-packages -p python3 env/
	source env/bin/activate
	which pip

```
(env) kallet@confmansys:~/collectorshaven$ which pip
/home/kallet/collectorshaven/env/bin/pip
```

	echo "django==3.2"  |tee requirements.txt
	pip install -r requirements.txt
	django-admin startproject collectorshaven
	cd collectorshaven/
	./manage.py startapp artglass
	./manage.py makemigrations
	./manage.py migrate
	./manage.py createsuperuser
	./manage.py runserver

![pic 1. Django @ localhost](/pics/pw2/4.png)  
*Django was running at localhost with admin enabled*  

So, then it was time to do some actual development. First I made a simple model with 2 fields, added that to admin.py and added my app to settings.py.

	micro collectorshaven/artglass/models.py 

```Python
#models.py
from django.db import models

class GlassItem(models.Model):
   name = models.CharField(max_length=300)
   manufacturer = models.CharField(max_length=300)
```

	micro collectorshaven/artglass/admin.py 
	
```Python
#admin.py
from django.contrib import admin
from . import models

admin.site.register(models.GlassItem)
```

	micro collectorshaven/collectorshaven/settings.py 

```Python
#settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artglass', #added this
]
```

After that I made database migrations to make my database ready for some cool glass objects.

```Bash
(env) kallet@confmansys:~/collectorshaven/collectorshaven$ ./manage.py makemigrations
Migrations for 'artglass':
  artglass/migrations/0001_initial.py
    - Create model GlassItem
(env) kallet@confmansys:~/collectorshaven/collectorshaven$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, artglass, auth, contenttypes, sessions
Running migrations:
  Applying artglass.0001_initial... OK
```

![pic 2. Added stuff to database](/pics/pw2/5.png)  
*Adding a GlassItem was working as expected*

After that I made some changes to print out a more reasonable admin view for my objects.

```Python
#models.py
from django.db import models

class GlassItem(models.Model):
   name = models.CharField(max_length=300)
   manufacturer = models.CharField(max_length=300)

#this defines the printout of all the objects in this class
   def __str__(self):
       return f"{self.name} {self.manufacturer}"
```

![pic 3. Added a default str-printout](/pics/pw2/6.png)  
*The string printout was much nicer than the previous one*

### Building views

According to [Karvinen](https://terokarvinen.com/) (lecture 24.5.2022) the right order to do this is (the route a request takes): user -> urls -> views -> models -> template. Since we don't have any idea what the user will be typing into their browser, we have to start with urls.py.

	micro collectorshaven/collectorshaven/urls.py 

```
#urls.py

from django.contrib import admin
from django.urls import path
from artglass import views

#these are the entrypoints the user uses (types into browser)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GlassItem.ListView.as_view()), 
]
```

That produced an error, as was expected. The error told me that artglass.views didn't have an attribute I was trying to use.

```
AttributeError: module 'artglass.views' has no attribute 'GlassItem'
```

Next, I added the view I was referring to in urls.py.

	micro collectorshaven/artglass/views.py 

```
#views.py

from django.views.generic import ListView #class based generic view
from . import models

class GlassItemListView(ListView): #inherits ListView
	model = models.GlassItem #in models.py
```

There was an error message, but I didn't  show progress as it didn't change.

```
AttributeError: module 'artglass.views' has no attribute 'GlassItem'
```

I decided to try out if my CamelCase was to blame and renamed my class in models.py.

```Python
#models.py

from django.db import models

class Artpiece(models.Model):
   name = models.CharField(max_length=300)
   manufacturer = models.CharField(max_length=300)

#this defines the printout of all the objects in this class
   def __str__(self):
       return f"{self.name} {self.manufacturer}"
```

```Python
#views.py

from django.views.generic import ListView #class based generic view
from . import models

class ArtpieceListView(ListView): #inherits ListView
	model = models.Artpiece #in models.py
```

I was still getting the same error, eventhought I had edited the files. That suggested to me that I had edited the wrong file. Looking at the error message more closely told me that maybe I had forgotten to change the name of my class in admin.py?

```
    admin.site.register(models.GlassItem)
AttributeError: module 'artglass.models' has no attribute 'GlassItem'
```

```Python
#admin.py
from django.contrib import admin
from . import models

admin.site.register(models.Artpiece)
```

Then I edited urls.py and didn't succeed.

```Python
#urls.py

from django.contrib import admin
from django.urls import path
from artglass import views

#these are the entrypoints the user uses (types into browser)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Artpiece.ListView.as_view()), 
]

```

```
  File "/home/kallet/collectorshaven/collectorshaven/collectorshaven/urls.py", line 8, in <module>
    path('', views.Artpiece.ListView.as_view()), 
AttributeError: module 'artglass.views' has no attribute 'Artpiece'
```

I started over. First I made  my urls.py & views.py.

```Python
#urls.py

from django.contrib import admin
from django.urls import path
from artglass import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ArtpieceListView.as_view()),
]
```

```Python
#views.py

from django.views.generic import ListView
from . import models

class ArtpieceListView(ListView): #inherits ListView
	model = models.Artpiece #in models.py

```

This time I managed to start the server.

![pic 4. templatedoesnotexist](/pics/pw2/7.png)  
**TemplateDoesNotExist at /**

So, that was a good sign. Next I created some folders and a template file.

	 cd /home/kallet/collectorshaven/collectorshaven/artglass
	 mkdir -p templates/artglass
	 micro templates/artglass/artpiece_list.html

```
Hello this a piece of art.
```

I had to restart the server, but after that I had a static page on my path.

![pic 5. templatedoesnotexist](/pics/pw2/8.png)  
*The template was working*

Next I added some fancier stuff in the shape of some actual content.

```
#artpiece_list.html

<h1>Artsy pieces on a list</h1>

{{ object_list }}
```

After that I made migrations and restarted the server, since I had changed the models earlier.

![pic 6. Template works](/pics/pw2/9.png)  
*The printed out the object*

I added some iteration for my template and more artse items to my database.

```
#artpiece_list.html
<h1>Artsy pieces on a list</h1>

{% for artpiece in object_list %}
    <p>Name: {{ artpiece.name }} <br> Manufacturer: {{ artpiece.manufacturer }}</p>
{% empty %}
	<p>No art yet!</p>
{% endfor %}

```

![pic 7. Template works](/pics/pw2/10.png)  
*The iterated list*

I quit after dinner & a revision @ 19.10.



