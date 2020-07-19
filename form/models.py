from django.db import models

# Create your models here.

class Machine(models.Model):
    machine_name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    quality = models.CharField(max_length=5)
    performance = models.CharField(max_length=5)
    availability = models.CharField(max_length=5)
    oee = models.CharField(max_length=5)

    def __str__(self):
        return self.machine_name
    def calculate_oeee(self):
        return float(self.quality) * float(self.performance)*float(self.availability)

class Occurrence(models.Model):
    OCURRENCE_TYPES = (
        ('S', 'STOP'),
        ('R', 'RESUME'),
    
    )
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    type_of_ocurrence = models.CharField(max_length=200, choices = OCURRENCE_TYPES)
    note = models.CharField(max_length=200)

    def __str__(self):
        return self.type_of_ocurrence




