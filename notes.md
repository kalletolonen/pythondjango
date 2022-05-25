
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

-A site for renting out RV's
-An individual booking calendar for each vehicle
-Renter can set renting terms: minimum rent period, day price & pre-set car properties (travel outside host country, pets, 230-v electricity, navigation, etc. )
-Comments for renter and vehicles (peer reviewed rentals)
-Search for customers (user sets date of travel & budget + more properties if needed)
-Login for customers & renters & admin
-Email confirmations

#### Stretch goals

**Paymment integration**
- Renter gives an account number
- Rentee makes payment -> a reservation is populated 

### Miniproject option 2

-Wordle clone with word definitions
-Users can comment on words and suggest improvements
