from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Post(models.Model):

    STATUS_CHOICES = (
        ('published', 'Published'),
        ('pending', 'Pending')
    )
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField('Slug', max_length=300)
    content = models.TextField('Content')
    status = models.CharField('Status', choices=STATUS_CHOICES, default='published', max_length=20)
    tag = TaggableManager()
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)
    update_date = models.DateTimeField('Update date', auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-creation_date']

