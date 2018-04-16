from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language
from taggit.managers import TaggableManager


class Post(models.Model):

    STATUS_CHOICES = (
        ('published', 'Published'),
        ('pending', 'Pending')
    )
    title = models.CharField('Title', max_length=255)
    title_en = models.CharField('Title en', max_length=255)
    slug = models.SlugField('Slug', max_length=300)
    slug_en = models.SlugField('Slug en', max_length=300)
    content = models.TextField('Content')
    content_en = models.TextField('Content en')
    status = models.CharField('Status', choices=STATUS_CHOICES, default='published', max_length=20)
    tag = TaggableManager()
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)
    update_date = models.DateTimeField('Update date', auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_title(self):
        if get_language() == 'pt-br':
            return self.title
        return self.title_en

    def get_slug(self):
        if get_language() == 'pt-br':
            return self.slug
        return self.slug_en

    def get_content(self):
        if get_language() == 'pt-br':
            return self.content
        return self.content_en

    class Meta:
        ordering = ['-creation_date']

