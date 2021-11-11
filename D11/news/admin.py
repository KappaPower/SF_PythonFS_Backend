from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
  fields = ['author', 'title','dateCreated', 'categoryType']
  list_display = ('author', 'title','dateCreated','get_categories', 'categoryType')
  list_filter = ( 'categoryType','dateCreated','author')
  search_fields = ('author', 'title','text')

  def get_categories(self, obj):
    return '\n'.join([c.name for c in obj.postCategory.all()])
  # list_display = [field.name for field in Post._meta.get_fields()]

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(CatSub)
# Register your models here.
