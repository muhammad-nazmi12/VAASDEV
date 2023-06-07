from django.http import HttpResponse
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from django.views.generic import View
import io

from .models import Document

class DocumentExportView(View):
    def get(self, request, *args, **kwargs):
        #Retrieve all Document objects from the database
        documents = Document.objects.all()

        #Load the HTML template for the export page
        #template = get_template('export_document.html')
        
        #Render the template with the document data
        #html = template.render({'documents':documents})
        
        #Create an HTTP response with the rendered HTML content
        #response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment;filename="export_document.html"'
        #response.write(html)
        
        #Create a new PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="documents.pdf'
        
        #Generate the PDF content
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)
        
        #Write the document data to the PDF
        for document in documents:
            pdf.drawString(100,100,str(document))
        
        #Close the PDF and write it to the response
        pdf.showPage()
        pdf.save()
        pdf_data=buffer.getvalue()
        buffer.close()
        response.write(pdf_data)
        return response