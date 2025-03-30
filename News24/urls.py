from django.contrib import admin
from django.urls import path
from .import views
from News24 import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf.urls import handler404


try:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.home , name='home'), 
        
        path('all/' ,views.all , name='all'), 
        

        path('search/' ,views.search , name='search'), 
        path('Agriculture/' ,views.agri , name='agri'), 
        path('Anime/' ,views.anime , name='anime'), 
        path('Sports/' ,views.sports , name='sports'), 
        path('Bollywood/' ,views.bolly , name='bolly'), 
        path('India News/' ,views.india , name='india'), 
        path('Tech/' ,views.tech , name='tech'), 
        path('Healthy/' ,views.healthy , name='healthy'),  
        path('Cars News/' ,views.car , name='cars'),  
        path('read/' ,views.read , name='read'),  
    ] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
except:
 pass   



    