from django.db import models

from cities_main.models import City


class Airplane(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Airplane")
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set', verbose_name="From city")
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city_set', verbose_name="To city")
    travel_time = models.PositiveSmallIntegerField(verbose_name="Travel time", default=0)
    
    def __str__(self):
        return f'Airplane {self.name} from {self.from_city} to {self.to_city}'

    class Meta:
        verbose_name = ("Airplane")
        verbose_name_plural = ("Airplanes")
        ordering = ["name"]