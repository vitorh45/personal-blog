from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'creation_date', 'update_date')
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = (
            'tiny_mce/tinymce.min.js',
            'tiny_mce/init_tinymce.js',
        )

admin.site.register(Post, PostAdmin)