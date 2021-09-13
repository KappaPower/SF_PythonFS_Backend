from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter,DateFromToRangeFilter, NumberFilter, ChoiceFilter, AllValuesFilter
from django.contrib.auth.models import User
from django import forms

from .models import Post, Author, Category, Comment
# создаём фильтр
class PostFilter(FilterSet):
    dateCreated = DateFilter(label='Date', lookup_expr='gte', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    rating = NumberFilter(label='Rating', lookup_expr='gte')
    # dateCreated = DateFromToRangeFilter(label='Date',  widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    # quantity = NumberFilter(lookup_expr='gte',label='Quantity', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # categoryType = ModelChoiceFilter(queryset=Category.objects.all(),label='Category',  widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Post
        fields = ['author__authorUsername',  'categoryType']


class F(FilterSet):
  username = CharFilter(method='my_filter')
  class Meta:
    model = User
    fields = ['username']

  def my_filter(self, queryset, name, value):
    return queryset.filter(**{name: value})

class C(FilterSet):
    category = ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
      model = Post
      fields = ['category']

class D(FilterSet):
    date = DateFromToRangeFilter()

    class Meta:
      model = Comment
      fields = ['date']