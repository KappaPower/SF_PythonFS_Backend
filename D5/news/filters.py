from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFromToRangeFilter, NumberFilter
from django_filters.widgets import RangeWidget
from django.contrib.auth.models import User


from .models import Post, Category, Comment
# создаём фильтр


class PostFilter(FilterSet):
    rating = NumberFilter(label='Rating', lookup_expr='gte')
    dateCreated = DateFromToRangeFilter(label='Date', lookup_expr=(
        'icontains'), widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = ['author',  'categoryType']


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
