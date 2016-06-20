from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError 
from personal.forms import ContactForm 

def home(request):
	return render(request, 'personal/home.html')

def aboutme(request):
	return render(request, 'personal/aboutme.html')

def skills(request):
	return render(request, 'personal/skills.html')

def career(request):
	return render(request, 'personal/career.html')

def achievements(request):
	return render(request, 'personal/achievements.html')

def blog(request):
	return render(request, 'personal/blog.html')

def contact(request):
	#return render(request, 'personal/contact.html')
	if request.method == 'GET':
		form = ContactForm()
	else:		
		form = ContactForm(request.POST) 		
		if form.is_valid():
			first_name = form.cleaned_data['first_name']			
			last_name = form.cleaned_data['last_name']
			from_email = form.cleaned_data['from_email']
			subject = form.cleaned_data['subject']			
			message = 'FROM, '+first_name.upper()+' '+last_name.upper()+': '+form.cleaned_data['message']
			try:					
				send_mail(subject, message, from_email, ['topcodertapopadma@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return thanks(request)
	return render(request, "personal/contact.html", {'form':form})

def thanks(request):
	return render(request, 'personal/thanks.html')