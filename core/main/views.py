from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Product
# Create your views here.

def category(request):
    category_list = Category.objects.all()
    return render(request, 'main/category.html', context={
        'category_list':category_list
    })



def subcategory(request, category_id):
    category = get_object_or_404(Category, slug=category_id)
    # subcategory_list = category.sub_category.all()
    return render(request, 'main/subcategory.html', context={
        'category_list':category,
    })



def product(request, category_id, subcategory_id):
    category = get_object_or_404(Category, slug=category_id)
    subcategory = get_object_or_404(SubCategory, slug=subcategory_id)
    product_list = Product.objects.filter(category=category, subcategory=subcategory)
    return render(request, 'main/product.html', context={
        'product_list':product_list
    })