from django.shortcuts import render
from django.utils import timezone #added code
from .models import Post #added code; this includes the model we wrote
									#in models.py
#the dot before models means current directory or current application.
#Both views.py and models.py are in the same directory
#So we can use . and the name of file(without .py) 
#Then we import the name of the model(Post)

# Create your views here.
def post_list(request):

	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#above line is to want published blog posts sorted by published_date.
	#posts is a variable we created for our QuerySet. Treat this as the name of our QuerySet.
	
	# return render(request, 'blog/post_list.html', {}) 
	#above line is original code. now we add something

	return render(request, 'blog/post_list.html', {'posts': posts})
	#we added posts inside the {} for template to use it. 

	#this def takes request and returns a function render that will
	# render(put together) our template blog/post_list.html