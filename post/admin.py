# post/admin.py

from django.contrib import admin
from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'title', 'content', 'post_thumbnail', 'category', 'created_at', 'updated_at', )
    list_per_page = 5
    list_editable = ('category', )
    search_fields = ('user', )
    list_select_related = ['user', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_post_count', )
    ordering = ('name', )

    def category_post_count(self, category_id):
        return Post.objects.filter(category_id=category_id).count()

    category_post_count.short_description = '카테고리 별 게시글 수'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content', 'created_at', 'updated_at', )
    list_per_page = 10
    search_fields = ('author', )
    list_select_related = ['post', 'author']