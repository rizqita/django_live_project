from django.shortcuts import render,redirect, get_object_or_404
from .models import Masukan, Blog
from .forms import Inputfeedback
from django.http import Http404

# Create your views here.
def masuk(request):
    masukan = Masukan.objects.all()
    return render(request,'index.html',{'masukan':masukan})   

def listmasukan(request):
    if request.method == 'POST':
        form = Inputfeedback(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = Inputfeedback()
    return render(request, 'Hubungikami.html',{'form':form})

def jkw_center_main(request):
    blog = Blog.objects.all()

    return render(request,'index.html',{'blog':blog})   

def jkw_social_media(request):
    return render(request,'socialmedia.html')

def blog_detail(request,blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request,'blog_detail.html',{'blog':blog})