from django import forms
from models import Blog, Comments

class Add(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_type', 'blog_name', 'add_date', 'blog_text')


class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('add_date', 'comment',)