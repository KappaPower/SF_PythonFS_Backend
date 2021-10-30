from django.urls import path
from django.conf.urls import url
from .views import NewsList, PostAuthor,PostView, PostSearch, PostCreateView, PostDeleteView, PostUpdateView ,  PostTag, PostType, subscribe_to_category, unsubscribe_from_category,ProfileView#, send_emails

app_name = 'news'
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', NewsList.as_view(), name='news'),  # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostView.as_view()),
    path('post/<int:pk>', PostView.as_view(), name='post_view'),
    path('search/', PostSearch.as_view(), name='search'),
    path('search/<int:pk>', PostView.as_view()),

    path('add/', PostCreateView.as_view(), name='post_add'),  # Ссылка на создание товара

    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    # url(r'^post_author$', post_author),
    path('author/<int:pk>', PostAuthor.as_view(), name='author_name'),
    path('type/<str:name>', PostType.as_view(), name='post_type'),
    path('tag/<int:pk>', PostTag.as_view(), name='post_tag'),

    path('subscribe/<int:pk>', subscribe_to_category, name='sub_cat'),
    path('unsubscribe/<int:pk>', unsubscribe_from_category, name='unsub_cat'),
    path('profile/', ProfileView.as_view(), name='profile'),

]