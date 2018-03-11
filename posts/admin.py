from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'creation_date', 'update_date')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)