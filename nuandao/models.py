from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=28)
    author_email = models.EmailField(blank=True)
    author_introduction = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return ''+self.author_name


class Category(models.Model):
    category_name = models.CharField(max_length=63)
    article_count = models.IntegerField(editable=False,default=0)

    def __str__(self):
        return ''+self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return ''+self.tag_name


class Article(models.Model):
    author = models.ForeignKey(Author, null=True)

    publish_date = models.DateTimeField(null=True)
    last_edit_date = models.DateTimeField(null=True)

    article_title = models.CharField(max_length=48)
    article_subtitle = models.CharField(max_length=80, blank=True)
    article_describe = models.CharField(blank=True,max_length=200)
    article_data = UEditorField(blank=True)

    article_category = models.ForeignKey(Category, related_name='Category', null=True)
    article_tags = models.ManyToManyField(Tag, blank=True)
    article_show = models.BooleanField(default=True, verbose_name='是否公开显示')
    article_read_count = models.IntegerField(null=True, blank=True, verbose_name='浏览次数')

    @staticmethod
    def last_edited_articles(num=5):
        return Article.objects.all()[:num].order_by('last_edit_date')

    @staticmethod
    def last_publish_articles(num=5):
        return Article.objects.all()[:num].order_by('-publish_date')

    def __str__(self):
        return ''+self.article_title



