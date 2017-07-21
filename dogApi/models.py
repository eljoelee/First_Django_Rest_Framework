from django.db import models

class Dog(models.Model):
    dogName = models.CharField(max_length=100)
    dogInfo = models.TextField()
    dogPob = models.CharField(max_length=100)
    dogPersonality = models.TextField()

    def __str__(self):
        return self.dogName