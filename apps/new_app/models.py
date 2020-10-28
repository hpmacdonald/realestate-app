from django.db import models
from django.urls import reverse


class Location(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'location'
        verbose_name_plural = 'locations'
    
    def get_url(self):
        return reverse('real_estate:houses_by_category', args=[self.slug])

    
    def __str__(self):
        return '{}'.format(self.name)

class House(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    beds = models.TextField(blank=True)
    bath = models.TextField(blank=True)
    address = models.TextField(blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='house', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'house'
        verbose_name_plural = 'houses'

    def get_url(self):
        return reverse('real_estate:housedetails', args=[self.location.slug, self.slug])

    
    def __str__(self):
        return '{}'.format(self.name)

