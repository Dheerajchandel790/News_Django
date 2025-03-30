from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from news.models  import Categoery, News

from django.contrib.auth.models import User

def home(request):
    
        categoery = Categoery.objects.all()
        news = News.objects.all().order_by('-id')
        return render(request, 'index.html', {'categoery': categoery,'news': news })    

def all(request):
    
        categoery = Categoery.objects.all()
        news = News.objects.all().order_by('-id')
        return render(request, 'all.html', {'categoery': categoery,'news': news })    
    


def india(request):
    try:     
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'India News' ).order_by('-id')
        return render(request, 'india.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')
    
def bolly(request):
    try: 
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Bollywood' ).order_by('-id')
        return render(request, 'bolly.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')
    
def car(request):
    try: 
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Car' ).order_by('-id')
        return render(request, 'car.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')
    
def agri(request): 
    
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Agriculture' ).order_by('-id')
        return render(request, 'agri.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')

def tech(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Tech' ).order_by('-id')
        return render(request, 'tech.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')
    
def sports(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Sports' ).order_by('-id')
        return render(request, 'sports.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')

def anime(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Anime' ).order_by('-id')
        return render(request, 'anime.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')

def healthy(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Healthy' ).order_by('-id')
        return render(request, 'healthy.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')

def search(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.all()
        search = request.GET.get('search')
        search_items = News.objects.filter( title__icontains = search).order_by('-id')
        return render( request, 'search.html',
                  { 'search_items':search_items,
                   'news': news ,
                   'categoery' :  categoery, })
    except:
        return render(request, 'eorrr.html')
    
def read(request):
    try:
        if request.method == 'POST':
            y = request.POST.get('read')
            read_items = News.objects.get( pk = y)
    

        return render(request, 'read.html' , {'read_items':read_items})
    except:
        return render(request, 'eorrr.html')


def custom_404_view(request, expection=None):
    return render(request, 'eorrr.html' ,status = 404 )

