from django.shortcuts import render
from .models import Blog

# Create your views here.
def jkw_center_main(request):
    blog = Blog.objects.all()
    return render(request,'index.html',{'blog':blog})
def jkw_social_media(request):
    return render(request,'socialmedia.html')
# def jkw_blog_post(request):
#     blog = Blog.objects.all()
#     return render(request,'blog.html',{'blog':blog})
