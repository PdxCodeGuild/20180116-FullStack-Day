from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)