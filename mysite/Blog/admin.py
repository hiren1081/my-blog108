from django.contrib import admin
from .models import post, Comment

# Register your models here.
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'auther', 'publish', 'stetus')
    list_filter = ('stetus', 'created', 'publish', 'auther')
    search_fields = ('title', 'body'),
    prepopulated_fields = {'slug' : ('title',)}
    row_id_fields = ('auther',)
    date_hierarchy = 'publish'
    ordering = ('stetus', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')