from django.db import models


class About(models.Model):

    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')

    def __str__(self):
        return self.title


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