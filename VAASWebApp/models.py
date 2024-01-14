from django.db import models
from django.contrib.auth.models  import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import os

class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email= self.normalize_email(email)
        user = self.model(email=email,username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,username,password,**extra_fields)
        
# For Document Model
class Document(models.Model):
    filename = models.CharField(max_length=255, default="default_filename")
    document=models.FileField(upload_to='documents/')

class User(AbstractUser,PermissionsMixin):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email=models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
     # Add any other fields you need
    objects: UserManager = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
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
        return self.email

class AccidentReport(models.Model):
    CaseID = models.BigAutoField(primary_key=True)
    Title = models.CharField(max_length=255, default='')
    Description = models.TextField()
    DateTime = models.DateTimeField(auto_now_add=True)
    DateCreated = models.DateField(null=True)
    
    def __str__(self):
        return str(self.CaseID)
    
   
class Location(models.Model):
    Address = models.CharField(max_length=255,primary_key=True)
    States = models.CharField(max_length=255,default='')
    Longtitude= models.DecimalField(max_digits=9,decimal_places=6)
    Latitude = models.DecimalField(max_digits=9,decimal_places=6)
    CaseID = models.ForeignKey(AccidentReport, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.Address)
    
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
    PersonLevelInjuries = [
        ('',''),
        ('Minor','Minor'),
        ('Moderate','Moderate'),
        ('Severe','Severe'),
    ]
    InjuriesLevel = models.CharField(max_length=10,choices=PersonLevelInjuries,default='')
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
    VehicleLevelDamage = [
        ('',''),
        ('Minor','Minor'),
        ('Major','Major'),
    ]
    DamageLevel = models.CharField(max_length=10,choices=VehicleLevelDamage,default='')
    VehicleDamage = models.CharField(max_length=255,default='')
    CaseID = models.ForeignKey(AccidentReport, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return (self.VehicleID)
    
class ReferenceDoc(models.Model):
    ReferenceID = models.BigAutoField(primary_key=True)
    RefItem = models.FileField(upload_to='references/',null=True)
    OwnedBy = models.CharField(max_length=100,default='')
    
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
    
    def get_file_name(self):
        return self.RefItem.name.split('/')[-1]