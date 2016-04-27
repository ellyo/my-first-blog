from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

"""
Functions which request information from a specified HTML file, then referenced by urls.py.
Some define arguments which are used by the HTML files.
"""

def homepage(request):
    return render(request, 'blog/homepage.html')

def shop(request):
    return render(request, 'blog/shop.html')

def search(request):
    return render(request, 'blog/search.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  # Posts included are ones with published dates in past
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):  # Displays one specific post or returns 404 error if the post doesn't exist
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def surprise_me(request):  #Creates a randomly ordered list of all the posts and only shows one to produce a random post
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).order_by('?')[:1] 
    return render(request, 'blog/post_list.html', {'posts': posts})

def non_alcoholic(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(units__iexact='0').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

"""
Listing posts by mood:
If the mood field for a post contains the specified mood, the post is included in the list
"""

def happy_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='happy').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def fun_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='fun').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def excited_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='excited').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def hungry_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='hungry').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def lazy_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='lazy').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def tired_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='tired').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def party_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='party').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def fancy_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='fancy').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def pitcher_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='pitcher').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def flirty_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now()).filter(mood__icontains='flirty').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})





