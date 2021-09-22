from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.forms import forms
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView,  DeleteView, TemplateView


from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView


# импортируем недавно написанный фильтр
from .filters import PostFilter, F, C, D
from .forms import PostForm  # импортируем нашу форму
from .models import Post, Comment, Category, Author


class NewsList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreated')
    paginate_by = 10  # поставим постраничный вывод в один элемент
    # добавляем форм класс, чтобы получать доступ к форме через метод POST
    form_class = PostForm

    # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # вписываем наш фильтр в контекст
        context['filter'] = PostFilter(
            self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = PostForm
        return context


class PostView(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'



# дженерик для получения деталей о товаре
class PostSearch(ListView):
    template_name = 'news/search.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

    # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # вписываем наш фильтр в контекст
        context['filter'] = PostFilter(
            self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = PostForm

        return context

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас

class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'news/crud/post_create.html'
    form_class = PostForm
    success_url = '/news/'

    permission_required = ('news.add_post')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = Author.objects.get(authorUsername=self.request.user)
        # print(self.request.user)
        self.object.save()
        return super().form_valid(form)


# дженерик для редактирования объекта
class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'news/crud/post_create.html'
    form_class = PostForm
    success_url = '/news/'

    permission_required = ('news.change_post')

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(PermissionRequiredMixin, DeleteView ):
    template_name = 'news/crud/post_delete.html'
    success_url = '/news/'
    permission_required = ('news.delete_post')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

