from django.db import models

# Create your models here.
class Userform(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True, max_length=100)
    dob = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=13)

    def __str__(self):
        return self.email
