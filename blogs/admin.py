from django.contrib import admin
from .models import blog,likes,user_profile,notification
from tinymce.widgets import TinyMCE
from django.db import models
class BlogsAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["title", "pub_date"]}),
        ("Content", {"fields": ["content"]}),
        ("creator", {"fields": ["user"]}),
        ("background", {"fields": ["back"]})
    ]

    


admin.site.register(blog,BlogsAdmin)
admin.site.register(likes)
admin.site.register(user_profile)
admin.site.register(notification)
# Register your models here.
