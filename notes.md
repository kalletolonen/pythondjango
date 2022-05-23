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



## Tips

Jupyter for CLI
Godot for games
Bionic mechanic.com

cp -nv = doesn't overwrite files

MDN Django tutorials
Django documentation / foreign key


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
