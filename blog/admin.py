from django.contrib import admin

# Register your models here.
from blog import models

admin.site.register(models.User)
admin.site.register(models.Article)
admin.site.register(models.Comments)
