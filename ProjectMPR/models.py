from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
from django.utils import timezone
class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar
    class Meta:
        verbose_name = ("Ingredient")
        verbose_name_plural = ("Ingredients")
    def __str__(self):
        return self.name
class Burger(models.Model):
    title = models.CharField(max_length=250) # a varchar
    content = ArrayField(models.CharField(max_length=12, blank=False),
            size=12,) # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    category = models.ForeignKey(Category, default="general") # a foreignkey
    class Meta:
        ordering = ["-title"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called