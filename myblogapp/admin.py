from django.contrib import admin

from .models import Post
from .models import Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		('Post Content', {'fields':['title', 'slug', 'body']}),
		('Metadata', {'fields':['tags', 'pub_date', 'mod_date']}),
	]
	list_display = ('title', 'pub_date')
	prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
