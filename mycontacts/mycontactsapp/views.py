from django.http import HttpResponse
from .models import Contact

def index(request):
    #return HttpResponse('Hello World')
    # Display contacts
    mylist = ""
    for i in Contact.objects.all():
        mylist += i.first_name + ' ' + i.last_name + '<br>'
    return HttpResponse("All Contacts:<br>" + mylist)
