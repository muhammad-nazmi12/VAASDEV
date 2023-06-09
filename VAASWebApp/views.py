from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.core import serializers
from .forms import DocumentForm,AccidentReportSearchForm,ReferDocSearchForm,CoordinateForm,LPForm,DailyPieChartForm,WeeklyBarChartForm,MonthlyGraphBarForm,ACForm,PForm
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Document,AccidentReport,ReferenceDoc,Person,Vehicle,Location
from django.contrib import messages
from django.db.models import Count
import matplotlib.pyplot as plt
import geocoder

# Create your views here.

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            #User credentials are valid, log in the user
            login(request,user)
            return redirect('home')
        else:
            #User credentials are not valid
            error_message='Invalid username or password'
            return render(request,'main/login.html',{error_message:error_message})
    else:
        return render(request,'main/login.html')
    
@login_required
def home(request):
    username = request.user.username
    context = {'name':'Vehicle Accident Analysis System','username':username}
    return render(request,'main/home.html',context)

def logout_view(request):
    logout(request)
    return redirect('signin')

def sampledesign(request):
    return render(request,'main/sample_design.html')

def testing(request):
    return render(request,'sample.html')

@login_required
def mapview(request):
    #Handle Search Coordinate form submission
    if request.method == 'POST' and 'coordform_submit' in request.POST:
        coordform = CoordinateForm(request.POST)
        if coordform.is_valid():
             # Process the form data and perform actions for Search Coordinate
            longitude = coordform.cleaned_data['longitude']
            latitude = coordform.cleaned_data['latitude']
            # Process the coordinates as needed
            location = geocoder.osm([latitude,longitude],method='reverse')
            # Retrieve the address from the location object
            address = location.address
        else:
            coordform = CoordinateForm()
    #Handle Search Location form submission    
    if request.method=='POST' and 'locateform_submit' in request.POST:
        locateform = LPForm(request.POST)
        if locateform.is_valid():
            # Process the form data and perform actions for Search Location
            location=locateform.cleaned_data['location']
        else:
            locateform = LPForm()

    centerpoint = [5.5351995,108.5584311]
    context={'center_point':centerpoint,
             'form1':CoordinateForm(),
             'form2':LPForm()
            }
    return render(request,'main/mapviewpage.html',context)

@login_required
def reportlib(request):
    form1 = AccidentReportSearchForm(request.GET)
    form2 = ReferDocSearchForm(request.GET)
    refer_doc = ReferenceDoc.objects.all()
    accident_reports = AccidentReport.objects.all()
    
    #Retrieve the search query values from the form
    query1 = request.GET.get('search_query1')
    query2 = request.GET.get('search_query2')
    
    #Apply filtering based on search query
    if query1:
        accident_reports = accident_reports.filter(Title__icontains=query1)
    
    if query2:
       refer_doc=ReferenceDoc.objects.filter(title__icontains=query2)
   
    if form1.is_valid() and query1:
        sortby_order1=form1.cleaned_data['sortbyorder1']
        category1 = form1.cleaned_data['categoryorder1']
        case_id_value= form1.cleaned_data['case_id_value']
        title_value = form1.cleaned_data['title_value']
        datetime_value = form1.cleaned_data['datetime_value']
        
         
         #Apply additional filtering based on category1 and corresponding value
        if category1 == 'CaseID' and case_id_value:
             accident_reports = accident_reports.filter(caseid=case_id_value)
             
            #Apply sorting based on sortby_order1
             if sortby_order1 =='asc':
                accident_reports = accident_reports.order_by('CaseID')
             elif sortby_order1 == 'desc':
                accident_reports = accident_reports.order_by('-CaseID')  
                
        elif category1 == 'Title' and title_value:
            accident_reports = accident_reports.filter(title__icontains=title_value)
            
            #Apply sorting based on sortby_order1
            if sortby_order1 =='asc':
                accident_reports = accident_reports.order_by('Title')
            elif sortby_order1 == 'desc':
                accident_reports = accident_reports.order_by('-Title')  
        elif category1 == 'DateTime' and datetime_value:
            accident_reports = accident_reports.filter(datetime = datetime_value) 
            
            #Apply sorting based on sortby_order1
            if sortby_order1 =='asc':
                accident_reports = accident_reports.order_by('DateTime')
            elif sortby_order1 == 'desc':
                accident_reports = accident_reports.order_by('-DateTime')  
               
               
    if form2.is_valid():
        order2 = form2.cleaned_data['sortbyorder2']
        element_option2 = form2.cleaned_data['elementbyorder2']
        
        if order2 == 'asc':
            refer_doc = refer_doc.order_by('date')
        elif order2 == 'desc':
            refer_doc = refer_doc.order_by('-date')

        if element_option2 == 'RefNo':
            refer_doc = refer_doc.filter(field4 ='value4')
            pass
        elif element_option2 == 'OwnedBy':
            refer_doc= refer_doc.filter(field5 ='value5')
            pass
        elif element_option2 == 'CaseID':
            refer_doc = refer_doc.filter(field6 ='value6')
            pass
        
    context ={'accident_reports':accident_reports,'refer_doc':refer_doc,'form1':form1,'form2':form2}
    return render(request,'main/reportlib.html',context)

@login_required
def analytical(request):
    dailyform = DailyPieChartForm(request.GET or None)
    weeklyform = WeeklyBarChartForm(request.GET or None)
    monthlyform = MonthlyGraphBarForm(request.GET or None)
       
    if dailyform.is_valid():
        dailyoption = dailyform.cleaned_data['DailyByChoice']
     
        if  dailyoption == 'Mon':
            #accident_reports = accident_reports.filter(field1 ='value1')
            pass
        elif dailyoption == 'Tue':
            #accident_reports = accident_reports.filter(field2 ='value2')
            pass
        elif dailyoption == 'Wed':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif dailyoption == 'Thu':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif dailyoption == 'Fri':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif dailyoption == 'Sat':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif dailyoption == 'Sun':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        
    if weeklyform.is_valid():
        weeklyoption = weeklyform.cleaned_data['WeeklyByChoice']
           
        if  weeklyoption == 'W1':
            #accident_reports = accident_reports.filter(field1 ='value1')
            pass
        elif weeklyoption == 'W2':
            #accident_reports = accident_reports.filter(field2 ='value2')
            pass
        elif weeklyoption == 'W3':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif weeklyoption == 'W4':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        
    if monthlyform.is_valid():
        monthlyoption = monthlyform.cleaned_data['MonthlyByChoice']
            
        if  monthlyoption == 'Jan':
            #accident_reports = accident_reports.filter(field1 ='value1')
            pass
        elif monthlyoption == 'Feb':
            #accident_reports = accident_reports.filter(field2 ='value2')
            pass
        elif monthlyoption == 'Mar':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif monthlyoption == 'Apr':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif monthlyoption == 'May':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif monthlyoption == 'Jun':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif monthlyoption == 'Jul':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif monthlyoption == 'Aug':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif monthlyoption == 'Sep':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif monthlyoption == 'Oct':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif monthlyoption == 'Nov':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        elif monthlyoption == 'Dec':
            #accident_reports = accident_reports.filter(field3 ='value3')
            pass
        
    context ={'DailyForm':dailyform,'WeeklyForm':weeklyform,'MonthlyForm':monthlyform}
    return render(request,'main/analytical.html',context)

@login_required
def exportimport(request):
    if request.method=='POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exportimport')
    else:
        form=DocumentForm()
    return render(request,"main/exportimport.html",{"form":form})
        
    return render(request,'exportimport.html')

def upload_document(request):
    if request.method=='POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'The document has been imported.')
            return redirect ('home')
    else:
        form=DocumentForm()
    return render(request,"upload_document.html",{"form":form})

def export_document(request):
    queryset=Document.objects.all()
    serialized_data=serializers.serialize('json',queryset)
    response = HttpResponse(serialized_data,content_type='application/json')
    response['Content-Disposition']='attachment; filename="documents.json"'
    return response

def accident_types(request):
    type_counts=AccidentReport.objects.values('type').annotate(count=Count('id')).order_by('type')
    types=[item['type'] for item in type_counts]
    counts=[item['count'] for item in type_counts]
    
    #Create the pie chart using matplotlib
    fig, ax = plt.subplots()
    ax.pie(counts, labels=types, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title('Distribution of Accident Types')
    
    #Save the chart as an image file
    chart_file='accident_types.png'
    fig.savefig(chart_file)
    
    #Render the chart template with the chart image
    return render(request,'accident_types.html',{'chart_file':chart_file})

def testpopup(request):
    return render(request,'popup_window.html')

def map_view(request):
    return render(request,'testing/map.html')

def testpopup2(request):
    return render(request,'testing/testpopup.html')

@login_required
def createcase_view(request): 
    if request.method == 'POST':
        #Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        person_names = request.POST.getlist('person_name[]')
        person_ages = request.POST.getlist('person_age[]')
        person_genders = request.POST.getlist('person_gender[]')
        person_types = request.POST.getlist('person_type[]')
        driver_licenses = request.POST.getlist('driver_license[]')
        injury = request.POST.getlist('injuries[]')
        vehicle_model = request.POST.get('vehicle_model')
        vehicle_type = request.POST.get('vehicle_type')
        plate_number = request.POST.get('plate_number')
        vehicle_owner_name = request.POST.get('vehicle_owner')
        vehicle_damage = request.POST.get('vehicle_damage')
        location_name = request.POST.get('location_name')
        location_address = request.POST.get('location_address')
        location_longcoord = request.POST.get('location_longcoord')
        location_latcoord = request.POST.get('location_latcoord')
        ref_item = request.POST.get('ref_item')
        owned_by = request.POST.get('owned_by')
        ref_type = request.POST.get('ref_type')
        
        #Create an AccidentReport object and save it to the database
        accident_report = AccidentReport.objects.create(
            Title = title,
            Description = description
        )
        
        #Create a Person object and save it to the database
        for i in range(len(person_names)):
            
            person_name = person_names[i]
            person_age = person_ages[i]
            person_gender = person_genders[i]
            person_type = person_types[i]
            driver_license = driver_licenses[i]
            injuries = injury[i]
            
            person = Person.objects.create(
                PersonName = person_name,
                PersonAge = person_age,
                PersonGender = person_gender,
                PersonType = person_type,
                DriverLicense = driver_license,
                Injuries = injuries,
                CaseID = accident_report
            )
            
            person.save()
        vehicle_owner = Person.objects.get(PersonName=vehicle_owner_name)
        vehicle = Vehicle.objects.create(
            VehicleModel = vehicle_model,
            VehicleType = vehicle_type,
            PlateNumber = plate_number,
            VehicleOwnerName = vehicle_owner,
            VehicleDamage = vehicle_damage,
            CaseID = accident_report
        )
        
        location = Location.objects.create(
            LocationName = location_name,
            LocationAddress = location_address,
            CoordLong = location_longcoord,
            CoordLat = location_latcoord,
            CaseID = accident_report
        )
        
        referdoc = ReferenceDoc.objects.create(
            RefItem = ref_item,
            OwnedBy = owned_by,
            RefType = ref_type,
            CaseID = accident_report
        )
            
        # Save the model objects to the database
        accident_report.save()
        
        vehicle.save()
        location.save()
        referdoc.save()

        #Display a success message
        messages.success(request,'Data saved successfully!')
        
        return HttpResponseRedirect('/VAASDEV/search/') 
        #Return a response or redirect as needed
    else:
        
        return render(request,'createcase/popup.html')