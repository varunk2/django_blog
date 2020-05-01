from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from datetime import datetime

from .models import Posts

def index(request):
	return render(request, 'blog/index.html')

def about(request):
	return render(request, 'blog/about.html')

def services(request):
	return render(request, 'blog/services.html')

def posts(request):
	posts = Posts.objects.order_by('-created_at')[:5]
	result = {'posts': posts}
	return render(request, 'blog/posts.html', result)

def create(request):
	if request.method == "POST":
		title = request.POST['title']
		body = request.POST['body']
		cover_image = handle_uploaded_file(request.FILES['cover_image'])	

		post = Posts(title=title, body=body, user_id=None, cover_image=cover_image)
		post.save()

		return HttpResponseRedirect(reverse('blog:posts'))
		# return HttpResponse(request.FILES)
	
	return render(request, 'blog/create.html')

def show(request, blog_id):
	post = get_object_or_404(Posts, pk=blog_id)
	return render(request, 'blog/show.html', {'post': post})

def edit(request, blog_id):
	post = get_object_or_404(Posts, pk=blog_id)

	if request.method == "POST":
		# return HttpResponse(request)
		post.title = request.POST['title']
		post.body = request.POST['body']
		post.save()
		return HttpResponseRedirect(reverse('blog:posts'))

	return render(request, 'blog/edit.html', {'post': post})

def delete(request, blog_id):
	# return HttpResponse(request.path_info) 
	post = get_object_or_404(Posts, pk=blog_id)
	post.delete()
	return HttpResponseRedirect(reverse('blog:posts'))

def dashboard(request):
	posts = Posts.objects.order_by('-created_at')
	result = {'posts': posts}
	return render(request, 'blog/dashboard.html', result)


# File upload function
def handle_uploaded_file(file):
	dotIndex = file.name.find('.')
	uniqueId = '_' + datetime.now().strftime("%m%d%Y")
	fileName = file.name[:dotIndex] + uniqueId + file.name[dotIndex:]
	filePath = 'images/'+fileName

	with open(fileName, 'wb+') as destination:
		for chunk in file.chunks():
			destination.write(chunk)

	return fileName