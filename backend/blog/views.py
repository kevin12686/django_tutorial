from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from .models import Blog
from .serializers import BlogSerializer


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


class blogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogList(ListView):
    model = Blog
    template_name = 'blogList.html'
