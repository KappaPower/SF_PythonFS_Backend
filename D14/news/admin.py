from django.contrib import admin
from django.utils.translation import gettext as _
from .models import *
from modeltranslation.admin import TranslationAdmin # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)

class PostAdmin(TranslationAdmin):
    model = Post

    list_display = ('author', 'title','dateCreated','get_categories', 'categoryType')
    list_filter = ( 'categoryType','dateCreated','author')
    search_fields = ('author', 'title','text')

    def get_categories(self, obj):
      return '\n'.join([c.name for c in obj.postCategory.all()])


class CategoryAdmin(TranslationAdmin):
    model = Category


class CommentAdmin(TranslationAdmin):
    model = Comment



admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CatSub)
# Register your models here.
