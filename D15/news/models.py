from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy # импортируем «ленивый» геттекст с подсказкой

class Author(models.Model):
    authorUsername = models.OneToOneField(User, verbose_name=_('username'), on_delete=models.CASCADE)

    authorRating = models.SmallIntegerField(_('rating'), default=0)
    avatar = models.ImageField(_('avatar'),upload_to='static/img')
    
    def __str__(self):
      if(self.authorUsername.first_name and self.authorUsername.last_name):
        return f'{self.authorUsername.first_name} {self.authorUsername.last_name} ({self.authorUsername})'
      else: 
        return f'{self.authorUsername}'

    def update_rating(self):
        postRate = self.post_set.all().aggregate(postRating = Sum('rating')) 
        #  postrating?
        pRate = 0
        pRate += postRate.get('postRating')

        commentRate = self.authorUsername.comment_set.all().aggregate(commentRating = Sum('rating'))
        cRate = 0
        cRate += commentRate.get('commentRating')

        self.authorRating = pRate * 3 + cRate
        self.save()

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

class Category(models.Model):
    name = models.CharField(
      # 'категория',
      max_length=64, 
      unique=True, 
      help_text=_('category'),
      )
    subscribers = models.ManyToManyField(
      User, 
      verbose_name=pgettext_lazy('help text for Category subscribers', 'subscribers'), 
      related_name='subscribers',
      through='CatSub', 
      blank=True,
      )
    def subscribe(self):
        pass
    def get_category(self):
        return self.name

    def __str__(self):
        return f'{self.name}' 

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

class Post(models.Model):
    author = models.ForeignKey(
      Author, 
      verbose_name=pgettext_lazy('help text for Post author', 'author'),  
      related_name='author',
      on_delete=models.CASCADE)
    NEWS = 'NWS'
    ARTICLE = 'ART'
    REVIEW = 'RVW'
    CATEGORY_CHOICES = (
        (NEWS, _('News')),
        (ARTICLE, _('Article')),
        (REVIEW, _('Review')),
    )
    categoryType = models.CharField(verbose_name=_('type'),
        max_length=3, choices=CATEGORY_CHOICES, default=ARTICLE)

    dateCreated = models.DateTimeField(_('date'), default=timezone.now)
    text = models.TextField(_('text'), default='')
    title = models.CharField(_('title'), max_length=128)
    rating = models.SmallIntegerField(_('rating'), default=0)
    isUpdated = models.BooleanField(_('edited'), default=False)

    postCategory = models.ManyToManyField(Category,  verbose_name=_('category'),through='PostCategory')
    
    def like(self):
        self.rating += 1 
        self.save()
    
    def dislike(self):
        self.rating -= 1 
        self.save()
    
    def preview(self):
        return f'{self.text[0:125]} ... rating: {str(self.rating)}'
      
    def email_preview(self):
        return f'{self.text[0:50]}...'
      

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/post/{self.id}' 
    
    def get_cat(self):
        return self.categoryType

    def __str__(self):
        return f'{self.dateCreated.date()} :: {self.author} :: {self.title} {self.categoryType}' 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}') # затем удаляем его из кэша, чтобы сбросить его

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, verbose_name=_('corr_post'), on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, verbose_name=_('corr_category'), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.categoryThrough} -> {self.postThrough}'

    class Meta:
        verbose_name = _('post category')
        verbose_name_plural = _('post categories')

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, verbose_name=_('corr_post'), on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, verbose_name=_('login'), on_delete=models.CASCADE)
    text = models.TextField(_('text'))
    dateCreated = models.DateTimeField(_('date'), auto_now_add=True)
    rating = models.SmallIntegerField(_('rating'), default=0)

    def __str__(self):
        try:
            return self.commentPost.author.username
        except:
            return self.commentUser.username

    def like(self):
        self.rating += 1 
        self.save()
    
    def dislike(self):
        self.rating -= 1 
        self.save()

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class CatSub(models.Model):
    category = models.ForeignKey(Category, verbose_name=_('category'), on_delete = models.CASCADE, blank=True, null=True)
    subscriber = models.ForeignKey(User, verbose_name=_('subscriber'), on_delete = models.CASCADE, blank=True, null=True)

    def get_user(self):
      return self.subscriber

    def get_category(self):
      return self.category.name
    def get_cat(self):
      return self.category

    def __str__(self):
        return f'{self.subscriber} - {self.category.name}'

    class Meta:
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')