from django.contrib import admin
from .models import Category, Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':('title' ,)
        }
    list_display = ('author','title', 'category', 'created_at', )
    list_filter = ('category', 'author')
    list_editable = ('title', )
    

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)