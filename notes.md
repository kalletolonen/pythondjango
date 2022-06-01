## Notes

Gandhi for name server

## Python

ipython3 <- Jupyter

Dictionary = {"key": value, "key2": value2}

Doesn't call main if imported to another class  
```Python
if __name__ == "__main__":
	main()
```

```Python
import hellomain
#call function

hellomain.function()
```

How to give parameters from CLI.
```Python
import sys

sys.argv[0] #command line parameters
```

```Python
class Animal():
	age = 3
	pass #empty class

	def sound(self):
		return "Generic animal sound"

	def whatareyou(self):
		return "Animal"

class Cat(Animal): #inheritance
	def sound(self):
		return "miau"

animal = Animal() #Animal() is the class constructor
walrus = Animal()
walrus.age = 66
print(animal.sound())
cat = Cat()
print(cat.sound())
print(cat.whatareyou())
```

## Django

*Request*
User -> urls -> views -> models -> template

Empty value for model field: blank= True, null=True

Google: class based generic views

### Models

### Base template
in template folder
base.html

{% block content %}
This is the content that will be overwritten.
{% endblock content %}

**in other template**
{% extends "templates/myapp/base.html" %}

{% block content %}
other content
{% endblock content %}


### Views

"Default view"
urls.py
in path an empty string

**Detail view** (see new view below)
#urls.py
from app import views

path('asdf/',views.TaskListView.as_view()),
path('asdf/<int:pk>',views.TaskDetailView.as_view()), #int as primary key

app/views.py
import DetailView

class TaskDetailView(DetailView):
	models.MyModel

template:
{{ object }}



### Admin

### URLS

INCLUDES

from django.urls import path, includes
path('todo/, include("todo.urls")), #entrypoint to program

-> todo urls.py
-> the same as urls.py in project urls before

project/project/urls.py

```
#new view

from myapp import views

urlpatterns, add
path('customer/', views.CustomerListView.as_view()), #entrypoint to program

micro app/views.py
->
from django.views.generic import ListView #class based generic view
from . import models

class CustomerListView(ListView): #inherits ListView
	model = models.Customer #in models.py

Models ->
myapp
-> mkdir templates
-> mkdir myapp
crm/templates/crm #add another app folder
micro customer_list.html

{{ object_list  }}
```

## Templates

SINGLE VIEW
In Template
{% for i in object_list %}
	<p>
		<a href="{{ task.get_absolute_url }}">
		{{ i.attributenamefrommodels.py }}
		</a>
	</p>
{% endfor %}

In Models.py

def get_absolute_url(self):
	return f"/mypathfromurls.py/{self.pk}"


Functions to model (ie. calculating the energy use on a run)

UPDATE
In Template

{% for i in object_list %}
	<p>
		<a href="{{ task.get_absolute_url }}">
		{{ i.attributenamefrommodels.py }}
		<a href= "{{ task.get_absolute_url }}">Update</a>
		</a>
	</p>
{% endfor %}

In Urls
path('myapp/update/<int:pk>'), views.MyappUpdateView.as_view())

In views
import UpdateView

Class MyappUpdateView(UpdateView):
	model = models.MyModel
	fields = "__all__" #you can list fields later on

in Templete
myapp_form.html

<form method=post>{% csrf_token %} #token makes sure it's not a forged request
	
	{{ form.as_p }} #as paragraph
	{{ form.as_t }} #as table
	<input type="submit">

</form>

CREATE
In Template

myapp_list.html
<p>
	<a href="/myapp/new/">New</a>
</p>

In Urls
urls.py

add path
path('myapp/new'). views.MyappCreateView()), #typos

in Views
add class

DELETE
https://www.geeksforgeeks.org/deleteview-class-based-views-django/
in Template

<p>
	<a href="{{task.get_absolute_url}}/delete">Delete</a>
</p>

In Urls
path('myapp/<int:pk>/delete'). views.MyappDeleteView.as_View()), #typos

Views
Add import
Create class

in Template
create myapp_confirm_delete.html
{{ object }}

-> Django 3.0 documentation from Karvinen

## Tips

f5 bot

Apache bench

head #a command to list files with file name neatly, takes multiple params.

Jupyter for CLI
Godot for games
Bionic mechanic.com

cp -nv = doesn't overwrite files

MDN Django tutorials
Django documentation / foreign key

Explain parameters when using commands.

Explain professional terms.

Explain the purpose!

df -h #check disk status
free -h #check ram

pandoc for md to html
-> file.md -o target.html

fg brings the last process to foreground that was put to background with ctrl + z  in cli.

In Micro:
retab can fix indendation errors (mixed tabs & spaces)

varlog/warlog #sudo commands

template:
{% debug %}

tags and filters -> from Django-course materials
create view -> context/add context(?) you can bring stuff from db to create view

realpath gives the full path with file name in cli


### Network errors

Wikipedia internet protocol suite.
	
	ip a
	ip routes
	
1. Try out ping to your ip
2. Try out ping to router
3. Try out ping to 8.8.8.8
4. Try out host to known site
5. Try out: time host domain

## Django
- models is the file that contains models and forms  
- views make things visible

makemigrations makes files
migrate executes the changes

Project is the whole site
Apps are sub-programs

/project/project/urls.py
-> where the code begins





### Miniproject option 1

- A site for renting out RV's
- Login for admin

#### Stretch goals


**Models**
- Renter can set renting terms: minimum rent period, day price & pre-set car properties (travel outside host country, pets, 230-v electricity, navigation, etc. )
- Comments for renter and vehicles 

**User auth**
- Login for customers & renters & admin M

**Views**
- Booking calendar for vehicles M
- Renter can get easy total sums of key metrics M
- Customer can view their rents and key metrics M
- Peer reviews for renters and customers (Confirmed rent from the renter required) D
- Search for customers (user sets date of travel & budget + more properties if needed) D

**Prices**
-An individual price calendar for each vehicle (day price (week price is calculated from that)) D

**Confirmations**
-Email confirmations D

**Paymment integration**
- Renter gives an account number M
- Rentee makes payment -> a reservation is populated D
- I take a cut for the service that's provided D

### Miniproject option 2

-Wordle clone with word definitions
-Users can comment on words and suggest improvements


### Production install

Don't upload private key for settings.py anywhere public!

Karvinen.com -> production install

0. Fix server settings
1. local devdjango folder
2. Make sure your project name is same on server & locally
3. do your dev
4. Login to server
5. scp -r manage.py app/ project/ host@domain:/locationofchoice
6. touch wsgi
7. create superuser on the server
8. make migrations

On the next run:
1. Dev
2. makemigrations, migrate
3. ssh user@domain 'touch wsgi'
4. ssh user@domain 'source activate
5. ssh user@domain 'migrate' #no need for makemigrations
6. ssh ";"-character allows many commands at once, like &&

## Copying from dev to production

ssh-copy
scp -r file folder/ user@hostname:targetfolder/

rsync - install to host and target
rsync -v -a folder user@hostname:targetfolder -> -copy verbose -all

rsync -v -a --exclude=esim/settings.py --exclude=esim2/nononoo.txt folder user@hostname:targetfolder -> -copy verbose -all

micro Makefile in directory
```
all:
	rsync-command
```

make -> runs Makefile

## Login
1. Activate env
2. Test functionality
3. views.py

```
-import loginrequiredmixin

class View(LoginRequiredMixin, View):
	pass
```

4. urls.py

```
from django.contrib.auth.views  import LoginView

path('accounts/login/', LoginView.as_view())
```

5. login template
```
templates/registration/login.html
<form method=post> csrf-token
{{form.as_p}}
<input type=submit>
</form>
```

## Logout

1. Base.html -> logout link
/logout?next=/app/
-> or as parameter in urls.

2. urls.py

```Python
import logoutview
path('accounts/logout/', LoginView.as_view(next_page="nönönönöö")),
```

## Registration

1. base.html -> register link
2. urls

```
path('accounts/register/', views.CreateView.as_view()),
```

3. view.py
import django.auth.contribs.auth.form UserCreationForm

```
class registerView(CreateView):
	form_class = UserCreationForm
	template_name ="registration/register.html"
	success_url="loginpageurl/"
```

4. register.hmtl
```
copy form
```

## User Spesific Views
settings.py -> settings.LOGIN_REDIRECT_URL ="/nononon"
settings.py -> settings.LOGOUT_REDIRECT_URL ="/nononon"

1. models.py
```Python
from django.contrib.auth.models import User
class asdf():
	owner =  models.ForeignKey(User, on_delete=models.CASCADE)
```
2. Migrate
3. view.py

```Python
class yourview(CreateView):
List fields without owner

	def form_valid(self, form):
		form.instance.owner = self.request.user #who made the form request
		return super().form_valid(form) #call CreateView
```

## unique views

1. views.py
```Python
class MyClass (LoginRequiredMixin, ListView): #remove previous
	def get_queryset(self):
		return models.MyTask.objects.filter(owner=self.request.user)
	# YOU HAVE TO ADD QUERYSET TO ALL VIEWS!
	List, Single, Update, Delete
```






Kuvien lisääminen on aika helppoa onnistuu Pillow kirjastolla ja ImageFieldillä, tossa esimerkki: 
https://github.com/kajami/python-course

Making queries

./manage.py shell
esineen perään
tabulaattori
? help
?? source code

touch wsgi local
copy rsync exclude db + settings.py
ssh -> source -> ./manage.py migrate
