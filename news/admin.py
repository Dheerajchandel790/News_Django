from django.contrib import admin

from .models import *

class CategoeryAdmin(admin.ModelAdmin):
    list_display = ["title", 'img']

class NewsAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'img','description','date']




admin.site.register(Categoery,CategoeryAdmin)
admin.site.register(News,NewsAdmin)

# Register your models here.
