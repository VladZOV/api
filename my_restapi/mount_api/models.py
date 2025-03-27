from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=150, verbose_name='Фамилия')
    name = models.CharField(max_length=150, verbose_name='Имя')
    otc = models.CharField(max_length=150, verbose_name='Отчество')
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'


class Coords(models.Model):
    latitude = models.FloatField(
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
        verbose_name='Долгота'
    )
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'Широта: {self.latitude}, Долгота: {self.longitude}, Высота: {self.height}'


class Level(models.Model):
    winter = models.CharField(max_length=10, blank=True, verbose_name='Зима')
    summer = models.CharField(max_length=10, blank=True, verbose_name='Лето')
    autumn = models.CharField(max_length=10, blank=True, verbose_name='Осень')
    spring = models.CharField(max_length=10, blank=True, verbose_name='Весна')

    def __str__(self):
        return f'Уровни: Зима-{self.winter}, Лето-{self.summer}, Осень-{self.autumn}, Весна-{self.spring}'


class Pereval(models.Model):
    STATUS_CHOICES = [
        ('new', 'новый'),
        ('pending', 'модератор взял в работу'),
        ('accepted', 'модерация прошла успешно'),
        ('rejected', 'модерация прошла, информация не принята'),
    ]

    beauty_title = models.CharField(max_length=255, blank=True, verbose_name='Красивое название')
    title = models.CharField(max_length=255, verbose_name='Название')
    other_titles = models.CharField(max_length=255, blank=True, verbose_name='Другие названия')
    connect = models.TextField(blank=True, verbose_name='Что соединяет')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new', verbose_name='Статус')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pereval')
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
    data = models.ImageField(upload_to='pereval_images/', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title
    