from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django. conf import settings

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'input.html')
class Send(View):
    def get(self,request):
        subject = 'Thankyou for contacting us'
        email_massage = 'we get in few moments'
        From_mail = settings.EMAIL_HOST_USER
        email = request.GET["t1"]
        to_list = [email]
        send_mail(subject,email_massage,From_mail,to_list,fail_silently=False)
        return HttpResponse("mail sent successfully")