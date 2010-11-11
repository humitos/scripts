from django.forms import ModelForm
from fmlatribu.posts.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post

