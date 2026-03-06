from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    course = models.CharField(max_length=50)
    date_of_admission = models.DateField()
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name