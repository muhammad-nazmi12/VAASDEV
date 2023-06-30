from django.db import models
from django.contrib.auth.models  import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# For Document Model
class Document(models.Model):
    filename = models.CharField(max_length=255, default="default_filename")
    document=models.FileField(upload_to='documents/')

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email=models.EmailField()
    
     # Add any other fields you need
    
    # Specify related_name for groups field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    
    # Specify related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Custom related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    def __str__(self):
        return self.username

class AccidentReport(models.Model):
    CaseID = models.BigAutoField(primary_key=True)
    Title = models.CharField(max_length=255, default='')
    Description = models.TextField()
    DateTime = models.DateTimeField(auto_now_add=True)
    DateCreated = models.DateField(null=True)
    
    def __str__(self):
        return str(self.CaseID)
    
   
class Location(models.Model):
    LocationName = models.CharField(max_length=255,primary_key=True)
    States = models.CharField(max_length=255,default='')
    CoordLong = models.FloatField(default=0)
    CoordLat = models.FloatField(default=0)
    CaseID = models.ForeignKey(AccidentReport, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.LocationName)
    
class Person(models.Model):
    PersonID = models.BigAutoField(primary_key=True)
    PersonName = models.CharField(max_length=255,default='',unique=True)
    PersonAge = models.PositiveIntegerField()
    PersonGenderChoice=[
        ('',''),
        ('Male','Male'),
        ('Female','Female'),
    ]
    PersonGender = models.CharField(max_length=10,choices=PersonGenderChoice)
    PersonTypeChoice=[
        ('',''),
        ('Driver','Driver'),
        ('Passenger','Passenger'),
        ('Biker','Biker'),
    ]
    PersonType= models.CharField(max_length=10,choices=PersonTypeChoice)
    DriverLicense = models.CharField(max_length=255,default='')   
    Injuries = models.TextField()
    CaseID = models.ForeignKey(AccidentReport, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.PersonID)
    
class Vehicle(models.Model):
    VehicleID = models.BigAutoField(primary_key=True)
    VehicleModel = models.CharField(max_length=255,default='')
    VehicleTypeChoice = [
        ('',''),
        ('Car', 'Car'),
        ('Motorcycle','Motorcycle'),
        ('Bus','Bus'),
        ('Truck','Truck'),
        ('Van','Van'),
        ('Other','Other'),
    ]
    VehicleType = models.CharField(max_length=20,choices=VehicleTypeChoice)
    VehiclePlateNumber = models.CharField(max_length=10,default='')
    VehicleOwner=models.CharField(max_length=255,default='')
    VehicleDamage = models.CharField(max_length=255,default='')
    CaseID = models.ForeignKey(AccidentReport, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return (self.VehicleID)
    
class ReferenceDoc(models.Model):
    ReferenceID = models.BigAutoField(primary_key=True)
    RefItem = models.FileField(upload_to='reference_docs/',null=True)
    OwnedBy = models.CharField(max_length=100,default='')
    ContactNumber = models.CharField(max_length=20,default='')  # New field for contact number
    
    RefTypeChoice = [
        ('',''),
        ('Document','Document'),
        ('Picture','Picture'),
        ('Video','Video'),
        ('Other','Other'),
    ]
    RefType = models.CharField(max_length=20,choices=RefTypeChoice)
    CaseID = models.ForeignKey(AccidentReport, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.ReferenceID)