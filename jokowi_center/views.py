from django.shortcuts import render
from .models import Masukan, Blog
from .forms import Inputfeedback 

# Create your views here.
# def jkw_center_main(request):
#     return render(request,'Hubungikami.html',{})
def listmasukan(request):
    if request.method == 'POST':
        form = Inputfeedback(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect ('halaman_feedback')
    else:
        form = Inputfeedback()
    return render(request, 'Hubungikami.html',{'form':form})

def jkw_center_main(request):
    blog = Blog.objects.all()
    return render(request,'index.html',{'blog':blog})

def jkw_social_media(request):
    return render(request,'socialmedia.html')
# def jkw_blog_post(request):
#     blog = Blog.objects.all()
#     return render(request,'blog.html',{'blog':blog})
