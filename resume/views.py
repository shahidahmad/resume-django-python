from django.shortcuts import render, redirect, render_to_response
from resume.models import ContactMe
from django.contrib import messages
from django.core.mail import send_mail
from django.template import RequestContext

def index(request):
    return render(request, 'home.html')

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def thank(request):
    return render(request, 'thankyou.html')

def send(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email_add = request.POST.get('email_add')
        message = request.POST.get('message')
        contact_obj = ContactMe(name= name, phone_number=phone, email_add=email_add, message=message)
        contact_obj.save()
        
        subject = "**Confirmation message**"
        firstName = name.split()[0]
        email_message = "Hi " + firstName + ",\n\nThank you for contacting me! \nYour message: \n\n\"" + message + "\"\n\n has been received. I will get back to you as soon as possible. \n\n\nKind regards, \nShahid Khan"
        from_email = email_add
        to_email = [from_email, "shahidahmads1@gmail.com"]

        send_mail(
            subject,
            email_message,
            from_email,
            to_email,
            fail_silently=False,
        )
        return render(request, 'thankyou.html')
