from django.contrib import admin
from .models import Blogger, Blog, Tag, BlogComment

admin.site.register(Tag)

# Register your models here.
class BlogInline(admin.TabularInline):
    model = Blog

# Define the admin class
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')
    field = ['name', 'date_of_birth']
#    inlines = [BlogInline]


# Register the admin class with the associated model
admin.site.register(Blogger, BloggerAdmin)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blogger', 'create_date')


#----------- Add Comment Admin -------------

