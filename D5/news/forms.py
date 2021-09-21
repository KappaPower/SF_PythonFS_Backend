from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from django import forms

from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    # author = user.id
    # forms.instance.name = request.user
# NOT NULL constraint failed: news_post.author_id
    # check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = [
          # 'author', 
          'categoryType', 
          'title', 
          'text' 
          ]

        widgets = {
          # 'author' : forms.Select(attrs={'class': 'form-control pure-input-1-2'}),
          'categoryType' : forms.Select(attrs={'class': 'form-control pure-input-1-2'}),
          'title' : forms.TextInput(attrs={'class': 'form-control pure-input-1-2',   'placeholder': 'Post Title'}),
          'text': forms.Textarea(attrs={'class': 'form-control pure-input-1-2'})
        }
        labels = {
                    # "author": "Author",
                    "categoryType": "Category",
                    "title": "Title",
                    "text": "Text",
                }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context["post_author"] = self.kwargs.get("username")
        return context
