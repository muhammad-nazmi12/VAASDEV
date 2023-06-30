from django.core.management.base import BaseCommand
from VAASWebApp.models import Location
import json

class Command(BaseCommand):
    help = 'Imports data from a JSON file'
    
    def add_arguments(self,parser):
        parser.add_argument('file_path',type=str,help='Path to the JSON file')
        
    def handle(self,*args,**options):
        file_path=options['file_path']
        
        with open(file_path) as file:
            json_data = json.load(file)
            
            for item in json_data:
                lat = item.get('lat')
                lng = item.get('lng')
                admin_name=item.get('admin_name')
                city = item.get('city')
                
                if lat and lng and city and admin_name:
                    location = Location(coordLat=lat,coordLong=lng,locationname=city,states=admin_name)
                    location.save()