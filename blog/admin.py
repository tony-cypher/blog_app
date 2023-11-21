from django.contrib import admin
from .models import Post, Comment, Team, Contact

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Team)
admin.site.register(Contact)