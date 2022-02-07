from django.db import models
from django.contrib import admin

class Teammate(models.Model):
    title = models.CharField(max_length=10, default="Mr.")
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.id} {self.title} {self.first_name} {self.last_name}"


class TeammateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'first_name', 'last_name')

# Create your models here.
