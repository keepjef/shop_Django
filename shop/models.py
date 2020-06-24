from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    carts = models.ManyToManyField('Cart', related_name='carts', verbose_name='Корзина')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(max_length=2000, db_index=True)
    image = models.ImageField(upload_to=None, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Cart(models.Model):
    title = models.CharField(max_length=100)


class ElementofCart(models.Model):
    pass


class User(models.Model):
    pass

