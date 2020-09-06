from django.contrib import admin
from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'user', 'photo')
    list_display_links = ('pk', 'user')

    list_editable = ('photo',)
    list_filter = ('created', 'modified')
