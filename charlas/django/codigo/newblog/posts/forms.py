from django.forms import ModelForm
from newblog.posts.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post

