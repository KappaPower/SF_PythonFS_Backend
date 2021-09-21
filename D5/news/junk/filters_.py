from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFromToRangeFilter, NumberFilter, ChoiceFilter, AllValuesFilter
from django.contrib.auth.models import User
from django import forms

from .models import Post, Author, Category, Comment

# создаём фильтр
class PostFilter(FilterSet):
    # title = CharFilter(label='Title', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # text = CharFilter(label='Text', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # authorUsername = ModelChoiceFilter(queryset=Author.objects.all(), label='Author',   widget=forms.Select(attrs={'class': 'form-control mb-2'}))     
    # # author = CharFilter(label='Author', lookup_expr='iexact')  
    # postCategory__name = ModelChoiceFilter(queryset=Category.objects.all(), label='Category')
    # dateCreated = AllValuesFilter(label='Date',widget=forms.Select(attrs={'class': 'form-control mb-2'}))    

    pass
    class Meta:
        pass
        # model = Post
        # fields = ('author__authorUsername','dateCreated', 'categoryType')
        # fields = ('author__authorUsername','dateCreated', 'categoryType')
        # fields = ('post_author', 'created')
        # fields = { 'author__authorUsername':['author'], 'categoryType':['contains'], 'rating':['gte'], }  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей) 

# from django import forms
# from django.utils.safestring import mark_safe

# class CustomModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return mark_safe("My Object custom label <strong>%i</strong>" % obj.id)


# class MyForm(forms.ModelForm):
#     my_field = CustomModelChoiceField(label=_('The form label'), queryset=MyModel.objects.filter(), widget=forms.RadioSelect, empty_label=None)
#     class Meta:
#         model = MyModel

class PostFilter(FilterSet):    
  dateCreated = DateFromToRangeFilter(label='Date',widget=forms.Select(attrs={'class': 'form-control mb-2'}))    
  # author = AllValuesFilter(label='Author',widget=forms.Select(attrs={'class': 'form-control mb-2'}))
  author__authorUsername = ModelChoiceFilter(queryset=Author.objects.all(), label='Author',   widget=forms.Select(attrs={'class': 'form-control mb-2'})    )        
  # categoryType = ModelChoiceFilter(queryset=Category.objects.all(),  label='Category',   widget=forms.Select(attrs={'class': 'form-control mb-2'})   )        
  class Meta:    
    model = Post           
    fields = ( 'dateCreated', 'categoryType')
    labels = {'author__authorUsername':'Author', 'dateCreated':'Date', 'categoryType':'Category'}