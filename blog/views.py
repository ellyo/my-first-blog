from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def mood_list(request):
    moods = ['Happy', 'Angry', 'Sad']
    return render(request, 'blog/mood_list.html', {'moods': moods})

def happy_list(request):
    posts = Post.objects.all().filter(mood__icontains='happy').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def angry_list(request):
    posts = Post.objects.all().filter(mood__icontains='angry').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def sad_list(request):
    posts = Post.objects.all().filter(mood__icontains='sad').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def fun_list(request):
    posts = Post.objects.all().filter(mood__icontains='fun').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def excited_list(request):
    posts = Post.objects.all().filter(mood__icontains='excited').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def hungry_list(request):
    posts = Post.objects.all().filter(mood__icontains='hungry').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def lazy_list(request):
    posts = Post.objects.all().filter(mood__icontains='lazy').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def tired_list(request):
    posts = Post.objects.all().filter(mood__icontains='tired').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def party_list(request):
    posts = Post.objects.all().filter(mood__icontains='party').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def fancy_list(request):
    posts = Post.objects.all().filter(mood__icontains='fancy').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def pitcher_list(request):
    posts = Post.objects.all().filter(mood__icontains='pitcher').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def flirty_list(request):
    posts = Post.objects.all().filter(mood__icontains='flirty').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

