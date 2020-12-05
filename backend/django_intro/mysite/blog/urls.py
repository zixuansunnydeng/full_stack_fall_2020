from django.urls import path, include

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('add', views.add, name='add'),
    path('posts/<int:post_id>', views.post, name='post'),
]