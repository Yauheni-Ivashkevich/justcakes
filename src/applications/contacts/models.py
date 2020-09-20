from django.db import models as m


class Contact(m.Model):
    """контакт"""
    title = m.CharField("Название", max_length=150, default='')
    phone = m.CharField("Телефон", max_length=150, default='')
    email = m.CharField("Почта", max_length=100, default='')
    vk = m.CharField("ВК", max_length=150, default='')
    instagram = m.CharField("Инстаграм", max_length=150, default='')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
