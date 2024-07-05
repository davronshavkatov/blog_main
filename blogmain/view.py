from django.shortcuts import render
from blogs.models import Category, Blog


def home(request):
    categoryes = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True).order_by('updated_at')
    context = {
        'categoryes':categoryes,
        'featured_posts':featured_posts
    }
    return render(request, 'home.html', context)
