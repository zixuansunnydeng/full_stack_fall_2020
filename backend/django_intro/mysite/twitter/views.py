from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm, TweetForm
from .models import Tweet, Follow

def index(request):
  return render(request, 'twitter/index.html')

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('twitter:index')
  else:
    form = UserCreationForm()
  return render(request, 'registration/signup.html', { 'form': form })

# page to create a new tweet as logged in user
def compose_tweet(request):
  current_user = request.user
  if not current_user.id:
    return redirect('/accounts/login')
  user = User.objects.get(id=current_user.id)
  if request.method == 'POST':
    form = TweetForm(request.POST)
    if form.is_valid():
      new_tweet = form.save(commit=False) # use commit=False to delay write (cuz we need to update the user field)
      new_tweet.user = user
      new_tweet.save()
      return redirect('twitter:user', current_user.id)
  else:
    form = TweetForm()
  context = {
    'form': form
  }
  return render(request, 'twitter/compose_tweet.html', context)

# tweet page, shows the tweet and all its comments
def tweet(request, tweet_id):
  tweet = get_object_or_404(Tweet, pk=tweet_id)
  comments= tweet.comments
  context = {
    'tweet': tweet,
    'comments': comments,
    'current_user': request.user,
  }
  # add comment as the current user
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      new_comment = form.save(commit=False)
      new_comment.tweet = tweet
      new_comment.user = request.user
      new_comment.save()
  else:
    form = CommentForm()
  context['comment_form'] = form
  return render(request, 'twitter/tweet.html', context)

def user(request, user_id):
  current_user = request.user
  user = get_object_or_404(User, pk=user_id)
  tweets = user.tweets.all()[:20]
  context = {
    'current_user': current_user,
    'user': user,
    'tweets': tweets,
  }
  # is the current user already following page's user
  already_following = Follow.objects.filter(user_from=current_user, user_to=user_id).exists()
  context['is_following'] = already_following
  if request.method == 'POST':
    if already_following:
      # unfollow
      follow = Follow.objects.get(user_from=current_user, user_to=user_id)
      follow.delete()
    else:
      # follow
      follow = Follow(user_from=current_user, user_to=user)
      follow.save()
    return redirect('twitter:user', user_id)
  return render(request, 'twitter/user.html', context)