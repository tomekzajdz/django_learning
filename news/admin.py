# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post
from .models import Comment

#Potrzebne do poprawnego wyświetlania stron z polskimi znakami,
#wygląda mało elegancko, ale działa
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = (u'title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)