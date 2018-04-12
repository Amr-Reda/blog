from django.shortcuts import render,redirect
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse

# Create your views here.
def article(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'article/article.html',{'articles':articles})


def details(request,slug):
    article =Article.objects.get(slug=slug)
    comment =Comment.objects.filter(article=article)
    form = forms.CreateComment()
    if request.method == 'POST':
        comment = forms.CreateComment(request.POST,request.FILES)
        instance = comment.save(commit=False)
        instance.author = request.user
        instance.article = article
        instance.save()
        comment = Comment.objects.filter(article=article)
        return render(request, 'article/details.html', {'article': article, 'comment': comment, 'form': form})
    else:
        return render(request,'article/details.html',{'article':article,'comment':comment,'form':form})


@login_required(login_url='/accounts/login')
def create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article:home')
    else:
        form = forms.CreateArticle()
    return render(request,'article/create.html',{'form':form})



    # if request.method == 'POST':
    #     comment=forms.CreateComment(request.POST)
    #     instance = comment.save(commit=False)
    #     instance.author = request.user
    #     instance.article = request.Article
    #     instance.save()
    #     return render(request,'article/details.html',{'article':article,'comment':comment})
    # else:
    #     return render(request, 'article/details.html', {'article': article})