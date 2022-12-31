from django.shortcuts import render, redirect
from blog.models import Post
from service.models import Service, Students
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def home_page(request):
    post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:3]
    service = Service.objects.all()
    students = Students.objects.all()
    print(post)
    #print(service)
    return render(request, 'home.html', {'post': post, 'service':service,  'students': students})


def about_page(request):
    return render(request, 'about.html')

def service_page(request):
    return render(request, 'services.html')

def contact_page(request):


	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'caps7751@gmail.com', ['caps7751@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})