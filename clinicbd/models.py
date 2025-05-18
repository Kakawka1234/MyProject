from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    age = models.IntegerField()
    owner_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} ({self.species})"


class Appointment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    def __str__(self):
        return f"Запис: {self.animal.name} Дата: {self.date.strftime('%Y-%m-%d %H:%M')}"
