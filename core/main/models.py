from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=30)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField('Category slug', unique=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-date']

class SubCategory(models.Model):

    category = models.ManyToManyField('Category', related_name='sub_category')
    name = models.CharField('SubCategory name', max_length=30)
    date = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_created=True)
    slug = models.SlugField('Category slug', unique=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        ordering = ['-date', '-date_created']

class Product(models.Model):

    category = models.ManyToManyField('Category', related_name='category_product')
    subcategory = models.ManyToManyField('SubCategory', related_name='subcategory_product')
    name = models.CharField('Product name', max_length=30)
    price = models.FloatField('Product price')
    image = models.ImageField('Product image', upload_to='main_images')
    slug = models.SlugField('Category slug', unique=True, null=True)


    def __str__(self):
        return self.name


