from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from news.models  import Categoery, News

from django.contrib.auth.models import User

def home(request):
    
        categoery = Categoery.objects.all()
        news = News.objects.all().order_by('-id')
        topNews = News.objects.all().order_by('-id')[:5]
        return render(request, 'index.html', {'categoery': categoery,'news': news ,  'topNews': topNews })    

def all(request):
    try:
        topNews = News.objects.all().order_by('-id')[:5]
        categoery = Categoery.objects.all()
        news = News.objects.all().order_by('-id')
        return render(request, 'all.html', {'categoery': categoery,  'topNews': topNews,'news': news })    
    except:
        return render (request, 'eorrr.html')

def india(request):
    try:
        topNews = News.objects.all().order_by('-id')[:5]
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'India News' ).order_by('-id')
        return render(request, 'india.html', {'categoery': categoery,'news': news , 'topNews': topNews })
    except:
        return render(request, 'eorrr.html')
    
def bolly(request):
    try: 
        topNews = News.objects.all().order_by('-id')[:5]
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Bollywood' ).order_by('-id')
        return render(request, 'bolly.html', {'categoery': categoery,'news': news , 'topNews': topNews})
    except:
        return render(request, 'eorrr.html')
    
def car(request):
    try: 
        topNews = News.objects.all().order_by('-id')[:5]
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Car' ).order_by('-id')
        return render(request, 'car.html', {'categoery': categoery,'news': news , 'topNews': topNews })
    except:
        return render(request, 'eorrr.html')
    
def agri(request): 
    
    try:
        topNews = News.objects.all().order_by('-id')[:5]
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Agriculture' ).order_by('-id')
        return render(request, 'agri.html', {'categoery': categoery,'news': news  , 'topNews': topNews })
    except:
        return render(request, 'eorrr.html')

def tech(request):
    try:
        categoery = Categoery.objects.all()
        topNews = News.objects.all().order_by('-id')[:5]
        news = News.objects.filter( Categoery__title = 'Tech' ).order_by('-id')
        return render(request, 'tech.html', {'categoery': categoery,'news': news , 'topNews': topNews })
    except:
        return render(request, 'eorrr.html')
    
def sports(request):
    try:
        topNews = News.objects.all().order_by('-id')[:5]
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Sports' ).order_by('-id')
        return render(request, 'sports.html', {'categoery': categoery,'news': news , 'topNews': topNews })
    except:
        return render(request, 'eorrr.html')

def anime(request):
    try:
        topNews = News.objects.all().order_by('-id')[:5]
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Anime' ).order_by('-id')
        return render(request, 'anime.html', {'categoery': categoery,'news': news , 'topNews': topNews })
    except:
        return render(request, 'eorrr.html')

def healthy(request):
    try:
        topNews = News.objects.all().order_by('-id')[:5]
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Healthy' ).order_by('-id')
        return render(request, 'healthy.html', {'categoery': categoery,  'topNews': topNews ,'news': news })
    except:
        return render(request, 'eorrr.html')

def search(request):
    try:
        categoery = Categoery.objects.all()
        topNews = News.objects.all().order_by('-id')[:5]
        news = News.objects.all()
        search = request.GET.get('search')
        search_items = News.objects.filter( title__icontains = search).order_by('-id')
        return render( request, 'search.html',
                  { 'search_items':search_items,
                   'news': news ,
                   'categoery' :  categoery
                    , 'topNews': topNews })
    except:
        return render(request, 'eorrr.html')
    
def read(request, x) :
    try:
        read_items = News.objects.get(pk = x)
        topNews = News.objects.all().order_by('-id')[:5]
        return render(request, 'read.html' , {'read_items':read_items , 'topNews': topNews})
    except:
        return render(request, 'eorrr.html')


def custom_404_view(request, expection=None):
    return render(request, 'eorrr.html' ,status = 404 )

