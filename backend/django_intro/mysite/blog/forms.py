from .models import Post
from django.forms import ModelForm, TextInput

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = [
      'title',
      'subtitle',
      'author',
      'content'
      ]
    widgets = {
      'title': TextInput(),
      'subtitle': TextInput(),
      'author': TextInput(),
    }