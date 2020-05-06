from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account hs been created! you are now able to log in.')
            return redirect('login')
    else:
        form  = UserCreationForm()
    return render(request,'register.html',{'form':form})
