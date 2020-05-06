from django.shortcuts import render
from django.http import HttpResponse
from .models import blogger
from django.contrib.auth.models import User
from .forms import BlogCommentsForm

# Create your views here.
def home(request):
    context = {
        'blogs': blogger.objects.all()
    }
    return render(request,'home.html',context)


def contact(request):
    return render(request,'contact.html')

def home1(request):
    return render(request,'home.html')



def blog(request):
    form= BlogCommentsForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'blog.html', context)
