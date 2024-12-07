from django.contrib import admin
from .models import Category
from django.utils.html import format_html
# Register your models here.

class CategryAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width=50 style="border-radius:50%">'.format(object.cat_img.url))
    list_display=('category_name','slug','description','thumbnail','cat_img')
    list_display_links=('category_name','slug','description','cat_img')
    prepopulated_fields={'slug':('category_name',)}
    ordering=('-category_name',)
    thumbnail.short_description='category Photo'
    

admin.site.register(Category,CategryAdmin)
