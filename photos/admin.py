from django.contrib import admin
from .models import Image,Location,Category,User

# Register your models here.
# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal=('categories',)

admin.site.register(User)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)
