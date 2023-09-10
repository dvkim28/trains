from django.db import models

from cities_main.models import City
from wagon.models import Airplane


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Route name")
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set',
                                  verbose_name="From city")
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set', verbose_name="To city")
    travel_times = models.PositiveSmallIntegerField(verbose_name="Total travel time", default=0)
    airplanes = models.ManyToManyField(Airplane, verbose_name='Airplane list')

    def __str__(self):
        return f'Route {self.name} from {self.from_city} to {self.to_city}'

    class Meta:
        verbose_name = ("Route name")
        verbose_name_plural = ("Routes")
        ordering = ["name"]