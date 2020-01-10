from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Ingredient")
        verbose_name_plural = ("Ingredients")
    def __str__(self):
        return self.name
class Burger(models.Model):
    title = models.CharField(max_length=250)
    ingredients = ArrayField(models.CharField(max_length=12, blank=False),size=12,)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    createdBy = models.ForeignKey(User, models.PROTECT, default=1)
    class Meta:
        ordering = ["-title"]
    def __str__(self):
        return self.title