from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
#if method is post
    if request.method == 'POST':
        form = PostForm(request.POST)
        if  form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
        # No, show ERROR
            return HttpResponseRedirect(form.erros.as_json())

    #Get all posts, limit = 20
    posts = Post.objects.all()[:20]

    #Show
    return render(request, 'posts.html',
            {'posts': posts})
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
