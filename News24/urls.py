from django.contrib import admin
from django.urls import path

from .import views
# from News24.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('<str:x>' , views.Dynamic_View), 
    path('search/' ,views.search , name='search'), 
    path('read/' ,views.read , name='read'), 
    
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
