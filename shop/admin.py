from django.contrib import admin
from .models import Product,Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    list_display_links = ['name']
    list_editable = ['slug']
    list_filter = ['name']
    list_per_page = 100
    list_max_show_all = 100
    date_hierarchy = 'publish_at'
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','publish_at','updated_at','stock','price']
    list_display_links = ['name']
    list_editable = ['price','stock']
    list_filter = ['name','category','publish_at']
    list_per_page = 100
    list_max_show_all = 100
    date_hierarchy = 'publish_at'
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}
    list_select_related = ['category']

    def category_name(self,obj):
        return obj.category.name
