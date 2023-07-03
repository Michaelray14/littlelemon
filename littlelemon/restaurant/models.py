from django.db import models

# Create your models here.
class Menu(models.Model):
    item = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    customer_name = models.CharField(max_length=200)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    table_number = models.IntegerField()