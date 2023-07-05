from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,FileResponse
from django.core import serializers
from .forms import DocumentForm,AccidentReportSearchForm,ReferDocSearchForm,CoordinateForm,LPForm,DailyPieChartForm,WeeklyBarChartForm,MonthlyGraphBarForm,UserSignUpForm
from django.contrib.auth import logout,authenticate,login,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .models import Document,AccidentReport,ReferenceDoc,Person,Vehicle,Location
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import geocoder
#import firebase_admin
#from firebase_admin import credentials

#User =  get_user_model

#specify the path to the service account key JSON file
#service_account_path = 'D:/Project/Python/secretkey/vaasdev-service-account-key.json'

#Initialize Firebase with the service account key
#cred = credentials.Certificate(service_account_path)
#firebase_admin.initialize_app(cred)

# Create your views here.
def signup(request):
    if request.method=='POST':
        signupform = UserSignUpForm(request.POST)
        if signupform.is_valid():
            username=signupform.cleaned_data.get('username')
            email = signupform.cleaned_data.get('email')
            password=signupform.cleaned_data.get('password')
            conpassword = signupform.cleaned_data.get('conpassword')
            
            #Check if the username is already taken
            if User.objects.filter(username=username).exists():
               error_message = 'Username is already taken'
               return render(request,'userform/signup.html',{'error_message':error_message})
            
            
            if conpassword==password:
                user = User.objects.create_user(username=username,email=email,password=password)
                
                #Send registration email to the user
                subject='Welcome to VAAS System'
                message='Thank you for registering on our website.'
                from_email=settings.DEFAULT_FROM_EMAIL
                recipient_list=[user.email]
                send_mail(subject,message,from_email,recipient_list)
                login(request,user)
                return redirect('home/')
            else:
                error_message = 'The password not same'
                return render(request, 'userform/signup.html',{'error_message':error_message}) 
        else:
            signupform=UserSignUpForm()
    
    return render(request,'userform/signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        #Authenticate the user
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            #User crdentials are valid, log in the user
            login(request,user)
            return redirect('home/')
        else:
            #User crededtials are not valid
            error_message="Invalid username or password"
            return render(request,'userform/signin.html',{'error_message':error_message})
    return render(request,'userform/signin.html')

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
    
    #Set the default selections for each dropdown
    daily_default=''
    weekly_default=''
    monthly_default=''
    
       
    if dailyform.is_valid():
        dailyoption = dailyform.cleaned_data['DailyByOrder']
     
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
        weeklyoption = weeklyform.cleaned_data['WeeklyByOrder']
           
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
        monthlyoption = monthlyform.cleaned_data['MonthlyByOrder']
            
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
        
    context ={
        'dailyform':dailyform,
        'weeklyform':weeklyform,
        'monthlyform':monthlyform,
        'daily_default':daily_default,
        'weekly_default':weekly_default,
        'monthly_default':monthly_default
        }
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

def AnalyticDoc(request):
    return render(request,'template/analyticpopup.html')

def get_analyticForm(request):
    option = request.GET.get('option')
    #Example 
    if option == 'Day':
        analyticform_template = 'exportfile/dailyreport.html'
    elif option == 'Week':
        analyticform_template = 'exportfile/weeklyreport.html'
    elif option == 'Month':
        analyticform_template = 'exportfile/monthlyreport.html'
    elif option == 'Year':
        analyticform_template = 'exportfile/yearlyreport.html'
    else:
        analyticform_template= ''
    
    form_html=render_to_string('exportfile/analyticform.html',{'analyticform_template':analyticform_template}) 
    return HttpResponse(form_html)

def analytic_report_preview(request):
    analytic_rep_preview = ''
    return HttpResponse(open(analytic_rep_preview,'rb'),conent_type='application/pdf')

def document_preview(request):
    document_path='media/DEAR_CUSTOMER.pdf'
    return FileResponse(open(document_path,'rb'),content_type='application/pdf')


def testpopup(request):
    return render(request,'popup_window.html')

def map_view(request):
    return render(request,'testing/map.html')

def testpopup2(request):
    return render(request,'testing/testpopup.html')

@login_required
def createcase_view(request): 
    if request.method == 'POST':
         # Retrieve the currently logged-in user
        current_user = request.user
        
        #Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        person_names = request.POST.getlist('person_name')
        person_ages = request.POST.getlist('person_age')
        person_genders = request.POST.getlist('person_gender')
        person_types = request.POST.getlist('person_type')
        driver_licenses = request.POST.getlist('driver_license')
        injury = request.POST.getlist('injuries[]')
        vehicle_models = request.POST.getlist('vehicle_models')
        vehicle_types = request.POST.getlist('vehicle_types')
        plate_numbers = request.POST.getlist('plate_numbers')
        vehicle_owners = request.POST.getlist('vehicle_owners')
        vehicle_damages = request.POST.getlist('vehicle_damages')
        location_name = request.POST.get('location_name')
        states = request.POST.get('states')
        location_longcoord = request.POST.get('location_longcoord')
        location_latcoord = request.POST.get('location_latcoord')
        ref_items = request.POST.getlist('ref_item')
        owned_by = request.POST.get('owned_by')
        ref_types = request.POST.getlist('ref_type')
        
        #Create an AccidentReport object and save it to the database
        accident_report = AccidentReport.objects.create(
            Title = title,
            Description = description
        )
        
        #Create a Person object and save it to the database
        if len(person_names)==len(person_ages)==len(person_genders)==len(driver_licenses)==len(person_types)==len(injury):
            for i in range(len(person_names)):
                
                person = Person()
                person.PersonName = person_names[i]
                person.PersonAge= person_ages[i]
                person.PersonGender = person_genders[i]
                person.PersonType= person_types[i]
                person.DriverLicense = driver_licenses[i]
                person.Injuries = injury[i]
                person.CaseID=accident_report
                person.save()
        else:
            # Handle the case when the lists have different lengths
            # Print an error message or perform appropriate error handling
            print("Error: Lengths of the lists are different.")
            
        if len(vehicle_models)==len(vehicle_types)==len(plate_numbers)==len(vehicle_owners)==len(vehicle_damages):
            for i in range(len(vehicle_models)):
                
                vehicle=Vehicle()
                vehicle.VehicleModel=vehicle_models[i]
                vehicle.VehicleType=vehicle_types[i]
                vehicle.VehiclePlateNumber=plate_numbers[i]
                vehicle.VehicleOwner = vehicle_owners[i]
                vehicle.VehicleDamage = vehicle_damages[i]
                vehicle.CaseID=accident_report
                #Check if the vehicle owner exists or create a new one
                vehicle_owner =get_object_or_404(Person,PersonName=vehicle.VehicleOwner)
                
                if vehicle_owner is None:
                    #Display an error message or handle the situation accordingly
                    return HttpResponse("Vehicle owner does not exists.")
                vehicle.save()
        else:
            # Handle the case when the lists have different lengths
            # Print an error message or perform appropriate error handling
            print("Error: Lengths of the lists are different.")
        
        location = Location.objects.create(
            LocationName = location_name,
            States = states,
            CoordLong = location_longcoord,
            CoordLat = location_latcoord,
            CaseID = accident_report
        )
        
        if len(ref_items)==len(ref_types):
            for i in range(len(ref_items)):
                referdoc=ReferenceDoc()
                referdoc.RefItem=ref_items[i]
                referdoc.OwnedBy= current_user.username
                referdoc.RefType=ref_types[i]
                referdoc.CaseID = accident_report
                referdoc.save()
        else:
            # Handle the case when the lists have different lengths
            # Print an error message or perform appropriate error handling
            print("Error: Lengths of the lists are different.")
            
        # Save the model objects to the database
        accident_report.save()

        location.save()
        

        #Display a success message
        messages.success(request,'Data saved successfully!')
        
        return HttpResponseRedirect('/search/') 
        #Return a response or redirect as needed
    else:
        
        return render(request,'createcase/popup.html')
    

def map_data_view(request):
    #Fetch the map data from a data source
    map_data={
        'latitude':5.5341995,
        'longitude':108.5584311,
    }
    
    #Return the map data as a JSON response
    return JsonResponse(map_data)

def generate_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            #Process form data
            data = form.cleaned_data
            
            #Generate the PDF document using ReportLab
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            
            p =  canvas.Canvas(response)
            p.drawString(100,750,'Document Content: ')
            p.drawString(100,700, data['content']) # Assuming 'content' is a form field
            p.showPage()
            p.save()
            
            return response
    else:
        form=DocumentForm()
        
    return render(request,'doctesting/generate_doc.html',{'form':form})
            
def daily_data(request):
    return render(request,'exportfile/dailyreport.html')

def weekly_data(request):
    return render(request,'exportfile/weeklyreport.html')

def monthly_data(request):
    return render(request,'exportfile/monthlyreport.html')

def yearly_data(request):
    return render(request,'exportfile/yearlyreport.html')
