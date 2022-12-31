from django.shortcuts import render
from .models import Service, Students


def service_page(request):
    services = Service.objects.filter()
    students = Students.objects.filter()
    

    return render(request, 'services.html', {'services':services, 'students':students })

def services_details(request, id):
    services = Service.objects.get(id=id)
  
    return render(request, 'services_details.html', {'services': services})




