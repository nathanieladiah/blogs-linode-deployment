from random import randint
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import TechPost
# Create your views here.
def index(request):
	return render(request, 'techblog/index.html')

def index(request):
	# In this blog 1 post will be featured at a time
	featured_post = TechPost.objects.filter(featured=True).first()

	posts = TechPost.objects.all().order_by('-created')
	paginator = Paginator(posts, 4)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	context = {'posts': posts, 'featured_post': featured_post}
	return render(request, 'techblog/index.html', context)

def post(request, slug):
	post = TechPost.objects.get(slug=slug)

	context={'post': post}
	return render(request, 'techblog/post.html', context)

def random(request):
	count = TechPost.objects.count()
	random_post = TechPost.objects.all()[randint(0, count-1)]

	return redirect('techblog:post', random_post.slug)
	# return HttpResponseRedirect(reverse("cs50game:post", args=(random_post.slug,)))