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
        path('search/' ,views.search , name='search'), 

        path('agri/' ,views.agri , name='agri'), 
        path('anime/' ,views.anime , name='anime'), 
        path('sports/' ,views.sports , name='sports'), 
        path('bolly/' ,views.bolly , name='bolly'), 
        path('india/' ,views.india , name='india'), 
        path('tech/' ,views.tech , name='tech'), 
        path('healthy/' ,views.healthy , name='healthy'),  
        path('read/' ,views.read , name='read'),  
    ] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
except:
 pass   



    