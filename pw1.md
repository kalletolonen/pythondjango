## pw1 Hello DJ A

I started @ 14.50.
  
The source for [the exercise](https://terokarvinen.com/2021/python-web-service-from-idea-to-production-2022/#pw1-hello-dj-a)
  
**Hardware & Software**  
*Win 11 + VirtualBox 6.0 + Debian 11 Bullseye*  
  
*Hardware:*  
*CPU: AMD Ryzen 9 5900HS*  
*Mem: 16 Gt LPDDR4X*  
*Storage: 512 Gt M.2 2230 NVMe PCIe 3.0 SSD*  

### a) Asenna Django-kehitysympäristö. / Install the Django development environment

First I needed to install VirtualEnv, so I did. A good tutorial to do this can be found here: https://terokarvinen.com/2022/django-instant-crm-tutorial/

	sudo apt-get update && sudo apt-get install -y virtualenv

After that I created a virtual environment for my Python.

	cd
	mkdir firstdjango
	cd firstdjango
	virtualenv --system-site-packages -p python3 env/

After that I activated the env.
	
	source env/bin/activate
	which pip

```
(env) kallet@confmansys:~/firstdjango$ which pip
/home/kallet/firstdjango/env/bin/pip
```

The printout confirmed that I was running pip from my env and not the system location. After this I had to fix a predefined version of Django for my project to ensure a long support life and install Django.
	
	echo "django==3.2" |tee requirements.txt
	pip install -r requirements.txt

```
(env) kallet@confmansys:~/firstdjango$ django-admin --version
3.2
```

That worked out, eventhought I had to change my VM to a fresh one that didn't have Django  already installed and messing up things.

### b) Lisää omia kenttiä malliin. / Add your own fields to the model

I did part c of this exercise first, so that I could check my models out in real time.

The process for for my app started by creating an app.

	./manage.py startapp rvrent
	micro rently/settings.py
	
I added my app to settings.py and localhost to ALLOWED_HOSTS (to mitigate the risk of deploying the application to a production environment with debug-features enabled)

```
ALLOWED_HOSTS = ['localhost', '127.0.0.1'] #added this

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rvrent', #added this
]

```

After that I edited my models.py and admin.py.
	
	micro rvrent/models.py
	micro rently/admin.py
	

```Python
#models.py
from django.db import models

class Rv(models.Model):
   name = models.CharField(max_length=300)
   reqLicense = models.CharField(max_length=30)
```


```Python
admin.py

from django.contrib import admin
from . import models

admin.site.register(models.Rv)
```

After these additions I did the database migrations, logged into my admin console and checked the results out.


![pic 4. Rvrent has a beginning](/pics/pw1/4.png)  
*My model was up and running*  

I decided to make a couple of changes to my model to add content.

	micro rvrent/models.py
		
```Python
#models.py

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
```

![pic 5. My model in action](/pics/pw1/5.png)  
*My console was looking relatively coherent*  


### c) Tee lisää käyttäjiä, jotka saavat kirjautua Djangon adminiin / Make users for admin-console

So, first I started a project.

	django-admin startproject rently
	cd rently/
	./manage.py runserver

![pic 1. Django @ localhost](/pics/pw1/1.png)  
*Django was running at localhost*  

After that I made the migrations and created a superuser.

	./manage.py makemigrations
	./manage.py migrate
	./manage.py createsuperuser

Now I had a superuser, so I tried to log in from the admin-console and add a few more superusers from there. The admin-console can be found at: http://127.0.0.1:8000/admin/

To add more users do the following steps:
1. Click "+ Add" on the Users in "AUTENTICATION AND AUTHORIZATION"
2. Insert the username & a good password
3. Click Save or Save and add another

To edit users and/or make the superusers  do these steps:
1. Click on Users
2. Select the user you'd like to edit
3. Select all the boxes in Permissions (Active, Staff Status and Superuser Status)
4. Save

![pic 2. Django supersuser rights](/pics/pw1/2.png)  
*A new superuser was added from the console*  

![pic 3. Django superuser had the right to add users](/pics/pw1/3.png)  
*The new admin could add users*  

