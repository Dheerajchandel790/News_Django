from django.shortcuts import render,redirect
from news.models  import Categoery, News

from django.contrib.auth.models import User

def home(request):
    categoery = Categoery.objects.all()
    news = News.objects.all()
    return render(request, 'index.html', {'categoery': categoery,'news': news })

def search( request):
    categoery = Categoery.objects.all()
    news = News.objects.all()
    search = request.GET.get('search')
    search_items = News.objects.filter( title__icontains = search)
    return render( request, 'search.html',
                  { 'search_items':search_items,
                   'news': news ,
                   'categoery' :  categoery, })

def read(request):
    if request.method == 'POST':
        y = request.POST.get('read')
        read_items = News.objects.get( pk = y)
    

    return render(request, 'read.html' , {'read_items':read_items})
    
    
def  Dynamic_View(request , x):
    categoery = Categoery.objects.all()
    news = News.objects.all()
    b = News.objects.filter(Categoery__title =  x)
    return render(request , 'dynamic.html ' , {'b':b , 'news': news ,'categoery': categoery})


def login_page(request):
    
    if request.method == 'GET':
        username = request.GET.get('username')
        passward = request.GET.get('passward')
    
    if User.objects.filter( username = username ).exists():
        return  redirect (request, 'index.html')

def reg(request):
    if request.method == 'GET':
        firstname = request.GET.get('first_name')
        lastname =request.GET.get('last_name')
        username = request.GET.get('username')
        
    
        user = User.objects.create(
             first_name = firstname,
             last_name  =lastname,
             username  = username,
            
             )
        user.save()

    return  render(request, 'register.html')