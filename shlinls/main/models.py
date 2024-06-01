from django.db import models
from django.contrib.auth.models import User

class Links(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField('Ссылка (до 250 символов)', max_length=250)
    slug = models.SlugField('Короткая ссылка', unique=True)

    def __str__(self):
        return f'{self.user} > {self.slug}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
