from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import BlogForm
from blog.models import Blog


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/index2.html', {'blog': blog})


def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit.html', {'blog': blog, 'form': form})


def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('product_list')
    return render(request, 'blog/delete.html', {'blog': blog})


def home(request):
    return HttpResponse('Hello Kitty!')