from django.db import models as m


class Cake(m.Model):
    """Вид десерта"""
    title = m.CharField("Название", max_length=150)
    prices = m.TextField("Стоимость и заказ", null=True, blank=True)
    description = m.TextField("Описание")
    image = m.ImageField("Изображение", upload_to="images/")
    # url = m.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Десерт"
        verbose_name_plural = "Десерты"


class Cake_name(m.Model):
    """Подвиды десертов"""
    title = m.CharField("Название десерта", max_length=100)
    ingredients = m.TextField("Описание ингредиентов", max_length=300)
    image = m.ImageField("Изображение", upload_to="images/")
    cake = m.ForeignKey(Cake, verbose_name="Десерт", on_delete=m.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подвид десерта"
        verbose_name_plural = "Подвиды десертов"


class Reviews(m.Model):
    """Отзывы"""
    email = m.EmailField("Название десерта", max_length=100)
    name = m.CharField("Имя", max_length=100)
    text = m.TextField("Сообщение", max_length=5000)
    parent = m.ForeignKey(
        'self', verbose_name="Родитель", on_delete=m.SET_NULL, blank=True, null=True
    )
    cake = m.ForeignKey(Cake, verbose_name="Десерт", on_delete=m.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.cake}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
