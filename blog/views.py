from django.shortcuts import render, get_object_or_404
from django.http import Http404
from  .models import Post

def index(request):
    posts = Post.published.all()
    return render(request, "blog/index.html",
                  {'posts':posts})


def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    return render(request, "blog/post/detail.html",
                 {'post':post})



def contact(request):
    return render(request, "blog/contact.html")

