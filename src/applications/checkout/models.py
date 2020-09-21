from django.db import models as m
from applications.index.storages import OverwriteStorage


class CheckoutInfoOption(m.Model):
    """опции информации о покупке"""
    title = m.CharField('Название опции', max_length=150, null=False, blank=False)
    description = m.TextField('Описание опции', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "опции оплаты и доставки"
        verbose_name_plural = "опции оплаты доставки"



class CheckoutInfo(m.Model):
    """модель информации об оплате"""
    title = m.CharField('Название', max_length=150, null=False, blank=False)
    description = m.TextField('Описание', null=True, blank=True)
    image = m.ImageField('Изображение', storage=OverwriteStorage(), upload_to=".")
    options = m.ManyToManyField(CheckoutInfoOption)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "информация об оплате и доставке"
        verbose_name_plural = "информация об оплате и доставке"
