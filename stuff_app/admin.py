from django.contrib import admin

# Register your models here.
from .models import Stuff,Post
# Register your models here.
admin.site.register(Stuff)
admin.site.register(Post)