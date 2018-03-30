from django.db import models


class About(models.Model):

    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')

    def __str__(self):
        return self.title
