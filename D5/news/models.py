from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUsername = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.SmallIntegerField(default=0)
    avatar = models.ImageField(upload_to='static/img')
    
    def __str__(self):
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


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    # authorUsername = models.OneToOneField(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'NWS'
    ARTICLE = 'ART'
    REVIEW = 'RVW'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
        (REVIEW, 'Обзор'),
    )
    categoryType = models.CharField(
        max_length=3, choices=CATEGORY_CHOICES, default=ARTICLE)

    dateCreated = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    text = models.TextField(default='')
    title = models.CharField(max_length=128)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1 
        self.save()
    
    def dislike(self):
        self.rating -= 1 
        self.save()
    
    def preview(self):
        return f'{self.text[0:125]} ... rating: {str(self.rating)}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/post/{self.id}' 


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        try:
            return self.commentPost.author.authorUsername.username
        except:
            return self.commentUser.username

    def like(self):
        self.rating += 1 
        self.save()
    
    def dislike(self):
        self.rating -= 1 
        self.save()
