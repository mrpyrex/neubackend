from django.contrib import admin
from .models import Post, PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'featured')
    list_filter = ('author', 'category', 'published', 'featured')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
