from django.contrib import admin
from .models import Category, SubCategory, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name', 'price']
    search_fields = ['id', 'name', 'price']



