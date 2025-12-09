from django.db import models


# Создание таблиц для базы данных
#  создание базы категорий
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Найменування")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="посилання URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорію"
        verbose_name_plural = "Категорії"

        #правильный вывод имени для категорий 
    def __str__(self):
        return f'{self.name}'


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Найменування")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="посилання URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Короткий опис")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Фото"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Ціна"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Акція %"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категорія"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

        #правильный вывод имени для продукции 
    def __str__(self):
        return f'{self.name},  Кількість:({self.quantity})'
