from django.db import models

# Create your models here.
class Xizmatlar(models.Model):
    title = models.CharField(max_length=25)
    img = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=75)

    def __str__(self):
        return self.title    
    
class Doctors(models.Model):
    img = models.ImageField(upload_to='images/')
    name_doctor = models.CharField(max_length=25)
    specialty = models.CharField(max_length=25)
    instagram_link = models.URLField(max_length=150)
    telegram_link = models.URLField(max_length=150)
    facebook_link = models.URLField(max_length=150)

    def __str__(self):
        return f"{self.name_doctor} - {self.specialty}"
    
class Contact(models.Model):
    user_name = models.CharField(max_length=25)
    patient_name = models.CharField(max_length=30)
    patient_about = models.CharField(max_length=255)
    patient_number = models.PositiveIntegerField(max_length=12)

    def __str__(self):
        return f"{self.user_name} - {self.patient_name}"

    
class Book_Appointment(models.Model):
    doctorName =  models.ForeignKey('Doctors', on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=25)
    department_name = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField(max_length=12)
    symptoms = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.patient_name



    

