from email import message
from django.shortcuts import redirect, render
from email_app.models import Student
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def student(request):
    return render(request,'student.html')
def student_details(request):
    if request.method=='POST':
        name=request.POST['student_name']
        age=request.POST['age']
        email=request.POST['std_mail']
        p=Student(Name=name,Age=age,Email=email)
        p.save()
        return redirect('student_details')
def sndmail(request):
    if request.method=="POST":
        name=request.POST['student_name']
        age=request.POST['age']
        email=request.POST['std_mail']
        p=Student(Name=name,Age=age,Email=email)
        p.save()
        subject="Application for python developer"
        message="We have received your application for the post of software developer.Thank you for your interest in our company"
        send_mail(subject,message,settings.EMAIL_HOST_USER,[email])
        return redirect('/')
    return render(request,'student.html')