from django.contrib import admin

from .models import (
    Location, Address, Company, User, Todo,
    Post, Comment,
    Album, Photo
)
# Register your models here.
admin.site.register(Location)
admin.site.register(Address)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Todo)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(Photo)
