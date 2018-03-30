from django.contrib import admin
from .models import About, Contact


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'tiny_mce/tinymce.min.js',
            'tiny_mce/init_tinymce.js',
        )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass