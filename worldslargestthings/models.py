from django.db import models


class Thing(models.Model):

    CATEGORY_CHOICES = [
        ('animal', 'Animal'),
        ('food', 'Food'),
        ('trinket', 'Trinket'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    location_city = models.CharField(max_length=200)
    location_state_province = models.CharField(max_length=200)
    location_country = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='other')
    image = models.ImageField(upload_to='thingsImages/', null=True, blank=True)
    is_draft = models.BooleanField(default=True)


    def __str__(self):
        return f'Thing: {self.name} in {self.location_country}'
    
