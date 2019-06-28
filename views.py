from django.shortcuts import render
from uform.forms import Userformdd
from django.http import HttpResponse
from django.shortcuts import render, redirect
from uform.models import Userform
from django.core.mail import EmailMessage
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Userformdd(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            email = request.POST["email"]
            dob = request.POST["dob"]
            mobileno = request.POST["mobileno"]
            try:
                userform = Userform.objects.get(email=email)
                messages.success(request, f'email already exist {email}!')
                return redirect(index)      
            except Userform.DoesNotExist:
                p=int(dob[:4])
                q=p-2019
                if q>=18:
                    userform = Userform.objects.create(email=email, name=name, dob=dob, mobileno=mobileno)
                    to_email = form.cleaned_data.get('email')
                    mail_subject = ''
                    message = "your form has been created.Thank you"
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                    userform.save()
                    messages.success(request, f'your form has been created')
                    return redirect(index)
                else:
                    messages.success(request, f'Age should be greater than 18 year..')
                    return redirect(index)
    else:
        form = Userformdd()    
    return render(request,'home.html',{'form':form})
