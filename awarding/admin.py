from django.contrib import admin
from .models import Post,Rating,Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Profile)