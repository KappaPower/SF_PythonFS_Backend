from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from django import forms

from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = [
          'categoryType', 
          'title', 
          'text' 
          ]

        widgets = {
          'categoryType' : forms.Select(attrs={'class': 'form-control pure-input-1-2'}),
          'title' : forms.TextInput(attrs={'class': 'form-control pure-input-1-2',   'placeholder': 'Post Title'}),
          'text': forms.Textarea(attrs={'class': 'form-control pure-input-1-2'})
        }
        labels = {
                    "categoryType": "Category",
                    "title": "Title",
                    "text": "Text",
                }
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)  
    #     context["post_author"] = self.kwargs.get("username")
    #     return context
