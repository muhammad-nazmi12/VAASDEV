from django import forms
from VAASWebApp.models import Document,AccidentReport,Person,Location,Vehicle,ReferenceDoc

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=('filename','document')

class CoordinateForm(forms.Form):
    longtitude = forms.FloatField(label='Longtitude:')
    latitude = forms.FloatField(label='Latitude:')
    
class LPForm(forms.Form):
    location = forms.CharField(label="Location:")
    
class UserLoginFrm(forms.Form):
    username = forms.CharField(label="Username: ")
    password = forms.CharField(label="Password: ")

class AccidentReportSearchForm(forms.Form):
    search_query1 = forms.CharField(required=False,max_length=100,
                                   widget=forms.TextInput(attrs={'placeholder':'Search...'}))
    sortbychoices1 = [
         ('','Sort by'),
         ('asc','Ascending'),
         ('desc','Descending'),
     ]    
    
    sortbyorder1 = forms.ChoiceField(required=False,choices=sortbychoices1)
    
    #Add Another dropdown
    category1 = [
        ('','Select an option'),
        ('CaseID','Case No.'),
        ('Title','Title'),
        ('DateTime','DateTime'),
    ]
    
    categoryorder1 = forms.ChoiceField(required=False,choices=category1)
    
    case_id_value = forms.IntegerField(required=False) 
    title_value = forms.CharField(required=False) 
    datetime_value = forms.DateTimeField(required=False) 
    

    
class ReferDocSearchForm(forms.Form):
    search_query2 = forms.CharField(required=False,max_length=100,
                                   widget=forms.TextInput(attrs={'placeholder':'Search...'}))
    
    sortbychoices2 = [
         ('','Sort by'),
         ('asc','Ascending'),
         ('desc','Descending'),
     ]    
    
    sortbyorder2 = forms.ChoiceField(required=False,choices=sortbychoices2)
    
    #Add Another dropdown
    
    elementbychoices2 = [
        ('','Select an option'),
        ('RefNo','Ref No.'),
        ('OwnedBy','Owned By'),
        ('CaseID','Case No.'),
    ]
    
    elementbyorder2 = forms.ChoiceField(required=False,choices=elementbychoices2)

class DailyPieChartForm(forms.Form):
    DailyByChoice=[
        ('','Current Day'),
        ('Mon','Monday'),
        ('Tue','Tuesday'),
        ('Wed','Wednesday'),
        ('Thu','Thursday'),
        ('Fri','Friday'),
        ('Sat','Saturday'),
        ('Sun','Sunday')
    ]
    
    DailyByOrder = forms.ChoiceField(required=False,choices=DailyByChoice)



class WeeklyBarChartForm(forms.Form):
    WeeklyByChoice = [
        ('','Current Week'),
        ('W1','Week 1'),
        ('W2','Week 2'),
        ('W3','Week 3'),
        ('W4','Week 4'),
    ]
    
    WeeklyByOrder=forms.ChoiceField(required=False,choices=WeeklyByChoice)

class MonthlyGraphBarForm(forms.Form):
    MonthlyByChoice=[
        ('','Current Month'),
        ('Jan','January'),
        ('Feb','February'),
        ('Mar','March'),
        ('Apr','April'),
        ('May','May'),
        ('Jun','June'),
        ('Jul','July'),
        ('Aug','August'),
        ('Sep','September'),
        ('Oct','October'),
        ('Nov','November'),
        ('Dec','December'),
    ]
    MonthlyByOrder = forms.ChoiceField(required=False,choices=MonthlyByChoice)

class ACForm(forms.ModelForm):
    class Meta:
        model = AccidentReport
        fields = ['Title','Description']

class PForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['PersonName','PersonAge','PersonGender','PersonType','DriverLicense','Injuries']
        

class VForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=['VehicleModel','VehicleType','VehiclePlateNumber','VehicleOwner','VehicleDamage']

class LForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['LocationName','LocationAddress']

class RDForm(forms.ModelForm):
    class Meta:
        model = ReferenceDoc
        fields = ['RefItem','OwnedBy','RefType']
        