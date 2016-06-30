# from django.contrib import admin

# Register your models here.

#original code above

#this admin is used to add, edit, and delete posts we've just modeled.

from django.contrib import admin
from .models import Post  #notice we've imported the Post model that 
#was defined in the models file. import meaning just add that code here, as a shortcut, like doing include..blah blah.

admin.site.register(Post) #this is to make our model visible in the 
			#admin page. that's why we register the model with
			#admin.site.register(Post)
