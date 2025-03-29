from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from news.models  import Categoery, News

from django.contrib.auth.models import User




def home(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.all()
        return render(request, 'index.html', {'categoery': categoery,'news': news })    
    except:
        return render(request, 'eorrr.html')

def india(request):
    try:     
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'India News' )
        return render(request, 'india.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')
    
def bolly(request):
    try: 
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Bollywood' )
        return render(request, 'bolly.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')
    
def agri(request): 
    
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Agriculture' )
        return render(request, 'agri.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')

def tech(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Tech' )
        return render(request, 'tech.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')
    
def sports(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Sports' )
        return render(request, 'sports.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')

def anime(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Anime' )
        return render(request, 'anime.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')

def healthy(request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.filter( Categoery__title = 'Healthy' )
        return render(request, 'healthy.html', {'categoery': categoery,'news': news })
    except:
        return render(request, 'eorrr.html')

def search( request):
    try:
        categoery = Categoery.objects.all()
        news = News.objects.all()
        search = request.GET.get('search')
        search_items = News.objects.filter( title__icontains = search)
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
