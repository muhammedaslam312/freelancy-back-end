from django.db import models

# Create your models here.

class Carosel(models.Model):
    image = models.ImageField(upload_to='photos/carosel/')
    title = models.CharField(max_length=100,blank=True)
    added_date  =models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title