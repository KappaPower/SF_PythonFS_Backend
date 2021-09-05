from django.urls import path
from .views import NewsList, PostView

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    # path('', HomePageView.as_view(), name='home'),
    path('', NewsList.as_view()),  # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostView.as_view()),
    # path('<int:pk>', CommentView.as_view()),
]