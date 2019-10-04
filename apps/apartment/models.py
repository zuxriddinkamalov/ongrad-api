from django.db import models

from apps.shared.model import BaseModel


class Apartment(BaseModel):
    rooms = models.PositiveIntegerField()
    price = models.FloatField()
    address = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    year = models.DateField()
    max_floor = models.PositiveIntegerField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.rooms} комнатная"
