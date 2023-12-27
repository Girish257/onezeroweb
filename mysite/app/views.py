from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from django.conf import settings
from django. contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request, 'app/index.html')

def projects(request): 
    return render(request, "app/footer.html") 
  
def contact(request): 

    if request.method == 'POST':
        Name = request.POST.get('name')
        subject = 'Regarding your enquiry'
        message = f'Hi {Name}, Thank You for contacting us. We will connect to you soon.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get('email') ]
        send_mail( subject, message, email_from, recipient_list )

        Companyname = request.POST.get('companyname')
        Contact_Number = request.POST.get('contactnum')
        Product_Name = request.POST.get('productname')
        Email = request.POST.get('email')
        Message = request.POST.get('message')

        message1 = f'Hi One Zero Enterprises, {Name} posted an enquiry. his/her company name is {Companyname}. his/her email id is {Email}. his/her Contact Number is {Contact_Number}. he/she wanted this {Product_Name} and mesaage is {Message}.  '
        recipient_list1 = ['onezeroenterprises@gmail.com']

        send_mail( subject, message1, email_from, recipient_list1 )

        messages.success(
            request ,'sent successfully')
        
        return redirect("contact")
    else:
        return render(request, "app/enquiry.html")

    


def about(request):
    return render(request, "app/aboutus.html")