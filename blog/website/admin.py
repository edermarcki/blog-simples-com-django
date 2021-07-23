from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories']
    search_fields = ['title', 'sub_title', 'categories', 'deleted']

    def get_queryset(self, request):
        return Post.objects.all()

# Register your models here.
admin.site.register(Post, PostAdmin)