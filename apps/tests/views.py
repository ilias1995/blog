from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from forms import Add, Comment
from models import Blog, BlogType, Comments
from django.contrib.auth import login as auth_login, authenticate, logout




def add_blog(request):
    blogtype = BlogType.objects.all()
    if request.method == 'POST':
        form = Add(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/')
    else:
        form = Add()
    return render(request, 'add_blog.html', {'form': form, 'blogtype': blogtype})

def index(request):
    blogtype = BlogType.objects.all()
    return render(request, 'index.html', {'blogtype': blogtype})

def base(request):
    blogtyp = BlogType.objects.all()
    return render(request, 'base.html', {'blogtyp': blogtyp})

def type_blog(request, id):
    blogtype = BlogType.objects.all()
    blogtypes = BlogType.objects.all().get(pk=id)
    return render(request, 'types.html', {'blogtypes': blogtypes, 'blogtype': blogtype})


def type_id(request, id):
    blogtype = BlogType.objects.all()
    blog = Blog.objects.all().get(pk=id)
    comment = Comments.objects.all()
    if request.method == 'POST':
        form = Comment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.blog = blog
            instance.user = request.user
            instance.save()

    else:
        form = Comment()
    c = dict(comment=comment, blog=blog, blogtype=blogtype, form=form)
    c.update(csrf(request))
    return render(request, 'type_id.html', c)

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('<h3> you need login again </h3>')
    else:
        blogtype = BlogType.objects.all()
        return render(request, 'login.html', {'blogtype': blogtype})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request):
    blog = Blog.objects.filter(user=request.user)
    blogtype = BlogType.objects.all()
    return render(request, 'profile.html', {'blogtype': blogtype, 'blog': blog})

def delete(request, id):
    blogtype = BlogType.objects.all()
    authenticated_user_blog = Blog.objects.filter(user=request.user).get(pk=id).delete()
    return render(request, "delete.html", {'blog': authenticated_user_blog, 'blogtype': blogtype})


