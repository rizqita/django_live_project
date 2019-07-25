from django.shortcuts import render
from .models import Masukan
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