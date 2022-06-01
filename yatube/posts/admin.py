from xml.etree.ElementTree import Comment
from django.contrib import admin

from .models import Comment, Group, Post, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'group', 'author')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Follow)
