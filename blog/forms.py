from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:   #le dice a gjango qué campos deben ser usados en el formulario
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)