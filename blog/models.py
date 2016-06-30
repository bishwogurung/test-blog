# from __future__ import unicode_literals

# from django.db import models

# Create your models here.

#everything above was original code before.

from django.db import models
from django.utils import timezone
#class keyword indictaes that we are defining an object.
#Post is the name  of our model. always start the name with an uppercase letter.
#models.Model means that Post is a Django Model, so Django knows that it should be saved in the database.
#models.Model tells Django to make sure to save the model, Post in the database.

#author, text, title: these are properties of the model for objects.
#give each property a type of field, is it a string, a number, a date?
class Post(models.Model): #this line defines our model (it is an object.)
	author = models.ForeignKey('auth.User') #this is a link to another model
	title = models.CharField(max_length=200) #for text up to 200 char limit.
	text = models.TextField() #models.TextField() means its for a long text without a limit. sounds ideal for a blog post content. also ideal for the description.. for projectstem
	created_date = models.DateTimeField( 
		default=timezone.now) #this is a date and time.
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self): #def for function definition
		self.published_date = timezone.now()
		self.save()

	def __str__(self): #this will get us a text(string) with a Post title
		return self.title

#after following code above, type in python manage.py makemigrations 
# blog in the console, which will return the following output.
# Migrations for 'blog':
#   0001_initial.py:
#     - Create model Post
# This tells us that it created the model.
#django prepared a migration file that we now have to apply to our database.
 # type python manage.py migrate blog and the output should be.

#  Operations to perform:
#   Apply all migrations: blog
# Running migrations:
#   Rendering model states... DONE
#   Applying blog.0001_initial... OK

# yaya, our model, Post, is now in the database.


