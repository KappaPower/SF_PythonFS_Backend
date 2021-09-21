from django.urls import path
from django.conf.urls import url
from .views import IndexView
# from .views import NewsList, PostView, PostSearch, PostCreateView, PostDeleteView, PostUpdateView, user_list, product_list, comment_list, ProtectedView

urlpatterns = [
  path('', IndexView.as_view()),
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    # path('', NewsList.as_view()),  # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view

]