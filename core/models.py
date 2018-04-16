from django.db import models
from django.utils.translation import get_language


class About(models.Model):

    title = models.CharField('Title', max_length=200)
    title_en = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    content_en = models.TextField('Content')

    def __str__(self):
        return self.title

    def get_title(self):
        if get_language() == 'pt-br':
            return self.title
        return self.title_en

    def get_content(self):
        if get_language() == 'pt-br':
            return self.content
        return self.content_en


class Contact(models.Model):

    STATUS_CHOICES = (
        ('read', 'Read'),
        ('unread', 'Unread')
    )
    subject = models.CharField('Subject', max_length=200)
    email = models.EmailField('Email from')
    message = models.TextField('Message')
    status = models.CharField('Status', choices=STATUS_CHOICES, default='unread', max_length=20)
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)

    def __str__(self):
        return '{} from {}'.format(self.subject, self.email)

    class Meta:
        ordering = ['-creation_date']