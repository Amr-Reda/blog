from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
# Create your views here.
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            dj_login(request,user)
            return redirect('article:home')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            dj_login(request, user)
            if 'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('article:home')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def logout(request):
    if request.method == 'POST':
        dj_logout(request)
        return redirect('article:home')