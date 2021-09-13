from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView,  DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.models import User


from .models import Post, Comment, Author, Category
from .filters import PostFilter , F, C,D  # импортируем недавно написанный фильтр
from .forms import PostForm  # импортируем нашу форму

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreated')
    paginate_by = 10 # поставим постраничный вывод в один элемент
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST
    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['categories'] = Category.objects.all()
        context['form'] = PostForm
        return context

class PostView(DetailView):
  model = Post
  template_name = 'post.html'
  context_object_name = 'post'

class HomePageView(View):
  template_name = "index.html"


# дженерик для получения деталей о товаре
class PostSearch(ListView):
    template_name = 'search.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['categories'] = Category.objects.all()
        context['form'] = PostForm

        return context

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm

# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'crud/post_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'crud/post_delete.html'
    # queryset = Post.objects.get(pk=id)
    success_url = '/news/'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


def user_list(request):
  f = F(request.GET, queryset=User.objects.all())
  return render(request, 'user_t.html', {'filter': f})

def product_list(request):
  c = C(request.GET, queryset=Post.objects.all())
  return render(request, 'product_t.html', {'filter': c})

def comment_list(request):
  d = D(request.GET, queryset=Comment.objects.all())
  return render(request, 'comment_t.html', {'filter': d})
