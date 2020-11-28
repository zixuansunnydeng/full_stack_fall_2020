from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
  posts = Post.objects.all()
  return render(request, 'blog/index.html', { 'posts': posts })

def about(request):
  return render(request, 'blog/about.html')

def post(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'blog/post.html', { 'post': post })

def add(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():        
      form.save()
      return redirect('/blog')
  else:
    form = PostForm()
    return render(request, 'blog/add.html', { 'form': form })
