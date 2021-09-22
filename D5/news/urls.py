from django.urls import path
from django.conf.urls import url
from .views import NewsList, PostView, PostSearch, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', NewsList.as_view()),  # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostView.as_view()),
    path('post/<int:pk>', PostView.as_view()),
    path('search/', PostSearch.as_view(), name='search'),
    path('search/<int:pk>', PostView.as_view()),

    path('add/', PostCreateView.as_view(), name='post_add'),  # Ссылка на создание товара

    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),

]