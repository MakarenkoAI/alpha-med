from django.db import models
from django.utils import timezone


class Record(models.Model):
    MALE = (
		('Мужской','Мужской'),('Женский','Женский'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)

    male = models.CharField(max_length=50, choices = MALE)
    databirth = models.CharField(max_length=50)
    diagnose = models.CharField(max_length=50)
    features = models.CharField(max_length=50)

    #data = models.DateTimeField(auto_now_add=True)
    data = models.CharField(max_length=15)
    palata = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    rest = models.CharField(max_length=15)      

    def __str__(self):
        return(f'{self.id} {self.first_name} {self.last_name}')
    
    def age(age):
        today = timezone.now().date()
        today = today.replace(year = int(today.year) - int(age))
        return today
    
    
class Room(models.Model):
    patient = models.CharField(max_length=15)
    #patient = models.ForeignKey(Record, default=None, on_delete=models.CASCADE)
    data_in = models.CharField(max_length=15)
    room = models.CharField(max_length=15)
    phone_room = models.CharField(max_length=15)
    data_out = models.CharField(max_length=15)  
    reason = models.CharField(max_length=15) 

    def __str__(self):
        return(f'{self.room}')

class WithPatient(models.Model):
    first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
    def __str__(self):
        return(f'{self.first_name}')
    
class WithDate(models.Model):
    data = models.CharField(max_length=15)
    def __str__(self):
        return(f'{self.data}')

class WithAgeAndMale(models.Model):
    male = models.CharField(max_length=50, choices = Record.MALE)
    data = models.CharField(max_length=15)
    def __str__(self):
        return(f'{self.data} {self.male}')