from django.urls import path
from . import views

urlpatterns=[
    path('', views.category, name='CategoryPage'),
    path('subcategory/<slug:category_id>/', views.subcategory, name='SubCategoryPage'),
    path('product/<slug:category_id>/<slug:subcategory_id>/', views.product, name='ProductPage'),

]