from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    about = models.TextField(max_length=500)
    type=models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                   ('Non IT', 'Non IT'),
                                                   ("Mobiles Phone", 'Mobiles Phone')
                                                   ))

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '-' + self.location

class Employee(models.Model):
    name = models.CharField(max_length=222)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(('Manager', 'manager'),
                                                        ('Software Developer', 'SD'),
                                                        ('Project Leader', 'pl')
                                                        ))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
