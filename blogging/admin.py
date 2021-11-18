from django.contrib import admin

from blogging.models import Post, Category


class Category_Post_Relationship(admin.StackedInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        Category_Post_Relationship,
    ]


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    exclude = ('posts',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
