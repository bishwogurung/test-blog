from django.conf.urls import url
from . import views #from . means from the entire blog application, or blog section

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	#above line assigns a view called post_list to ^$ URL
	]
