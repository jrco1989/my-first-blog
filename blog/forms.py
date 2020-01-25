from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:   #le dice a gjango qué campos deben ser usados en el formulario
        model = Post
        fields = ('title', 'text',)