# from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Appointment(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField()
    Date = models.DateField()
    PhoneNo = models.IntegerField()
    Message = models.TextField(blank=True, null=True)
