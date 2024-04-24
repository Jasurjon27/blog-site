from django.contrib import admin
from models import Category, Tag, Author, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','cattegory','author')
    list_display_links = ('id','title','cattegory','author')
    filter_horizontal = ('tags',)
    search_fields = ('title','category','author')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post,PostAdmin)