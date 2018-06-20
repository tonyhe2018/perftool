from django.contrib import admin
from blog.models import Blog, Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_data','update_time')


admin.site.register(Blog)
admin.site.register(Article, ArticleAdmin)
