from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='категория', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(verbose_name='Наименование', max_length=128)
    image = models.ImageField(verbose_name='Фото', upload_to='products/')
    manufacturer_country = models.CharField(verbose_name='Страна-производитель', max_length=128)
    year_of_issue = models.IntegerField(verbose_name='Год выпуска')
    model = models.CharField(verbose_name='Модель', max_length=128)
    created_at = models.DateField(auto_now=True)
    in_stock = models.BooleanField(verbose_name='в наличии', default=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
