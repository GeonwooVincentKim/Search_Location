from django.contrib import admin
from .models import Post


# admin.site.register(Show_Location)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']
    # list_editable = ['is_public']


# admin.site.register(Post)

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'location', 'time']
#     list_display_links = ['location']
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'created_at']
# list_display_links = ['title']
