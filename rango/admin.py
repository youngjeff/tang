from django.contrib import admin


from rango.models import Category, Page, UserProfile
# Register your models here.


admin.site.register(Page)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)