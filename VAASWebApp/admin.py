from django.contrib import admin
from .models import Document,AccidentReport,Vehicle,Person,Location,ReferenceDoc

# Register your models here.
admin.site.register(Document)
admin.site.register(AccidentReport)
admin.site.register(Vehicle)
admin.site.register(Person)
admin.site.register(Location)
admin.site.register(ReferenceDoc)

