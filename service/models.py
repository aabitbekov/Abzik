import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категория'


class Maintenance(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Услуга')
    price = models.CharField(max_length=9, verbose_name='Цена')

    class Meta:
        verbose_name = 'услугу'
        verbose_name_plural = 'Услуги'


    def __str__(self):
        return self.name


class DoneMaintenance(models.Model):
    marka = models.CharField(max_length=114, verbose_name="Марка авто:")
    model = models.CharField(max_length=114, verbose_name="Модель авто:")
    year = models.IntegerField(verbose_name="Год автомобиля",
                               validators=[MinValueValidator(1900),
                                           MaxValueValidator(datetime.date.today().year)],
                               default=datetime.date.today().year)
    mileage = models.IntegerField(max_length=7, help_text='Пробег авто в км', blank=True, verbose_name='Пробег')
    maintenance = models.ForeignKey(Maintenance, verbose_name='Предоставленные услуги', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Предоставленные услуги'
        verbose_name_plural = 'Предоставленные услуги'

    def __str__(self):
        return '{}, {}, {}'.format(self.marka, self.model, self.year)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        recforavto = Recomendation()
        recforavto.marka = self.marka
        recforavto.model = self.model
        recforavto.year = self.year
        recforavto.mileage = self.mileage
        recforavto.maintenance = self.maintenance
        recforavto.save()
        super().save(force_insert, force_update, using, update_fields)


class Recomendation(models.Model):
    marka = models.CharField(max_length=114, verbose_name="Марка авто:")
    model = models.CharField(max_length=114, verbose_name="Модель авто:")
    year = models.IntegerField(verbose_name="Год автомобиля",
                               validators=[MinValueValidator(1900),
                                           MaxValueValidator(datetime.date.today().year)],
                               default=datetime.date.today().year)
    mileage = models.IntegerField(max_length=7, help_text='Пробег авто в км', blank=True, verbose_name='Пробег')
    maintenance = models.ForeignKey(Maintenance, verbose_name='Рекомендуемые услуги', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Рекомендуемые услуги'
        verbose_name_plural = 'Рекомендуемые услуги'


    def __str__(self):
        return '{}, {}, {}'.format(self.marka, self.model, self.year)