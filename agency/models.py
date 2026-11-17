from django.db import models

MAX_LENGTH = 255


class Country(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название страны')
    visa_required = models.BooleanField(default=True, verbose_name='Требуется виза')
    description = models.TextField(null=True, blank=True, verbose_name='Описание страны')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class TourCategory(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория тура'
        verbose_name_plural = 'Категории туров'


class Tour(models.Model):
    title = models.CharField(max_length=MAX_LENGTH, verbose_name='Название тура')
    description = models.TextField(null=True, blank=True, verbose_name='Программа и описание')
    price = models.FloatField(verbose_name='Стоимость (руб.)')
    duration_days = models.PositiveIntegerField(default=7, verbose_name='Длительность (дней)')
    photo = models.ImageField(upload_to='tours/%Y/%m/%d/', null=True, blank=True, verbose_name='Фотография тура')
    is_available = models.BooleanField(default=True, verbose_name='Доступен для бронирования')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Страна')
    category = models.ForeignKey(TourCategory, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f"{self.title} ({self.country.name} — {self.price} руб.)"

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Service(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование услуги')
    description = models.TextField(null=True, blank=True, verbose_name='Описание услуги')
    price = models.FloatField(verbose_name='Стоимость услуги (руб.)')
    processing_days = models.PositiveIntegerField(default=3, verbose_name='Срок оказания (дней)')
    is_active = models.BooleanField(default=True, verbose_name='Услуга активна')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Hotel(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название отеля')
    stars = models.PositiveIntegerField(default=4, verbose_name='Количество звёзд')
    address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес отеля')
    price_per_night = models.FloatField(verbose_name='Цена за ночь (руб.)')
    photo = models.ImageField(upload_to='hotels/%Y/%m/%d/', null=True, blank=True, verbose_name='Фотография отеля')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна расположения')

    def __str__(self):
        return f"{self.name} ({self.stars}*)"

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class Excursion(models.Model):
    title = models.CharField(max_length=MAX_LENGTH, verbose_name='Название экскурсии')
    description = models.TextField(null=True, blank=True, verbose_name='Описание маршрута')
    duration_hours = models.PositiveIntegerField(default=4, verbose_name='Длительность (часов)')
    price = models.FloatField(verbose_name='Стоимость (руб.)')
    photo = models.ImageField(upload_to='excursions/%Y/%m/%d/', null=True, blank=True, verbose_name='Фотография экскурсии')
    tours = models.ManyToManyField(Tour, blank=True, verbose_name='Входит в туры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экскурсия'
        verbose_name_plural = 'Экскурсии'


class OfficeEmployee(models.Model):
    full_name = models.CharField(max_length=MAX_LENGTH, verbose_name='ФИО сотрудника')
    position = models.CharField(max_length=MAX_LENGTH, verbose_name='Должность')
    phone = models.CharField(max_length=50, verbose_name='Рабочий телефон')
    email = models.EmailField(verbose_name='Электронная почта')
    photo = models.ImageField(upload_to='employees/%Y/%m/%d/', null=True, blank=True, verbose_name='Фотография сотрудника')

    def __str__(self):
        return f"{self.full_name} — {self.position}"

    class Meta:
        verbose_name = 'Сотрудник представительства'
        verbose_name_plural = 'Сотрудники представительства'


class EmployeeBadge(models.Model):
    employee = models.OneToOneField(OfficeEmployee, on_delete=models.CASCADE, related_name='badge', verbose_name='Сотрудник')
    badge_number = models.CharField(max_length=50, unique=True, verbose_name='Номер пропуска')
    access_level = models.CharField(max_length=100, default='Стандартный', verbose_name='Уровень доступа')
    issued_date = models.DateField(auto_now_add=True, verbose_name='Дата выдачи')

    def __str__(self):
        return f"Пропуск №{self.badge_number} ({self.employee.full_name})"

    class Meta:
        verbose_name = 'Служебный пропуск'
        verbose_name_plural = 'Служебные пропуска'