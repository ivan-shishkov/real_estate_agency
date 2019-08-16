from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    class Meta:
        verbose_name = 'квартира'
        verbose_name_plural = 'квартиры'

    created_at = models.DateTimeField('когда создано объявление', default=timezone.now, db_index=True)
    
    description = models.TextField('текст объявления', blank=True)
    price = models.IntegerField('цена квартиры', db_index=True)

    town = models.CharField('город, где находится квартира', max_length=50, db_index=True)
    town_district = models.CharField('район города, где находится квартира', max_length=50, blank=True, help_text='Чертаново Южное')
    address = models.TextField('адрес квартиры', help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField('этаж', max_length=3, help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField('количество комнат в квартире', db_index=True)
    living_area = models.IntegerField('количество жилых кв.метров', null=True, db_index=True)

    has_balcony = models.NullBooleanField('наличие балкона', null=True, db_index=True)
    active = models.BooleanField('активно ли объявление', db_index=True)
    construction_year = models.IntegerField('год постройки здания', null=True, db_index=True)

    new_building = models.NullBooleanField('является ли новостройкой')

    likes = models.ManyToManyField(User, verbose_name='кто лайкнул', blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    class Meta:
        verbose_name = 'жалоба'
        verbose_name_plural = 'жалобы'

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='кто жаловался')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, verbose_name='квартира, на которую пожаловались')
    text = models.TextField('текст жалобы')

    def __str__(self):
        return self.text[:30]


class Owner(models.Model):
    class Meta:
        verbose_name = 'владелец'
        verbose_name_plural = 'владельцы'

    full_name = models.CharField('ФИО владельца', max_length=200)
    phone_number = models.CharField('номер телефона владельца', max_length=20)
    normalized_phone_number = PhoneNumberField('нормализованный номер телефона владельца', blank=True)

    flats = models.ManyToManyField(Flat, related_name='owners', verbose_name='квартиры в собственности')

    def __str__(self):
        return self.full_name
