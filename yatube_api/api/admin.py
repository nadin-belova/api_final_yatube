from django.contrib import admin

from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "text",
        "pub_date",
        "author",
        # "group",
    )
    search_fields = ("text",)
    list_filter = ("pub_date",)
    # list_editable = ("group",)
    empty_value_display = "-пусто-"


# class GroupAdmin(admin.ModelAdmin):
#     list_display = (
#         "pk",
#         "title",
#         "slug",
#         "description",
#     )
#     search_fields = ("title",)
#     list_filter = ("title",)
#     list_editable = ("slug",)
#     empty_value_display = "-пусто-"


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "post",
        "author",
        "text",
        "created"
    )
    search_fields = ("post__text", "author__username")
    list_filter = ("created",)
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
# admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)