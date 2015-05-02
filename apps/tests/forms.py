from django import forms
from django.contrib.auth.models import User
from models import Blog, Comments

class Add(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_type', 'blog_name', 'add_date', 'blog_text')


class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('add_date', 'comment',)


class Register(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password')