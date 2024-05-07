from django.db import models
# создаём модель Phone с полями id, name, price, image, release_date, lte_exists и slug.
# Поле id — должно быть основным ключом модели.
# начение поля slug должно устанавливаться слагифицированным значением поля name.

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=75, default="default title")
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=19, decimal_places=1, default="0")
    image = models.URLField(max_length=200)
    release_date = models.DateField(auto_now=False, auto_now_add=False, default="01.01.2000")
    lte_exists = models.BooleanField()
