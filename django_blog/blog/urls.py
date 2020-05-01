from django.urls import path

from . import views

app_name='blog'
urlpatterns = [
	path('', views.index, name='index'),
	path('about', views.about, name='about'),
	path('services', views.services, name='services'),
	path('posts', views.posts, name='posts'),
	path('create_post', views.create, name='create_post'),
	path('<int:blog_id>/', views.show, name='show'),
	path('<int:blog_id>/edit', views.edit, name='edit'),
	path('<int:blog_id>/delete/', views.delete, name='delete'),
	path('dashboard', views.dashboard, name='dashboard'),
]
