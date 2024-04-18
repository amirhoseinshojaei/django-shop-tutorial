from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250,db_index=True)
    slug = models.SlugField(db_index=True)
    publish_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('publish_at',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'your category name {self.name} and published at {self.publish_at}'

    def get_absolute_url(self):
        return reverse('shop:products_by_category',args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(db_index=True)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    publish_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        ordering = ('publish_at',)
        index_together = (('id','slug'),)
        verbose_name = 'product'
        verbose_name_plural= 'products'

    def __str__(self):
        return f'product name is {self.name} and published to {self.publish_at}'

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])
