def handle_uploaded_file(f):
 with open("some/fie/name.txt","wb+") as destination:
     for chunk in f.chunks():
         destination.write(chunk)