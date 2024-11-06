from django.db import models
from django.contrib.auth.hashers import make_password

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)  # Automatically incrementing ID
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class ServiceProvider(models.Model):
    sp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    adhar_card = models.CharField(max_length=12)  # Assuming it's a 12-digit number
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)  # Adjust if needed
    mobile = models.CharField(max_length=15)  # Adjust as per your needs
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Will be hashed before saving
    skills = models.TextField()  # Allows for multiple skills in a text format

    def save(self, *args, **kwargs):
        if self.pk is None:  # Only hash password if the object is new
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class ServiceHistory(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sp_id = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField()
    pending_completion = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.service} by {self.sp_id} for {self.client}"
