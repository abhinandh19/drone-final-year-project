from django.shortcuts import render
from mysite import settings
from django.http import HttpResponse
from django.core.mail import send_mail

def mail(request):
    subject= "hello"
    msg = "new product has been added"
    to = "buddytech30@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if (res==1):
        msg = "MAIL SENT"
    else:
        msg = "MAIL NOT SENT"
    return HttpResponse(msg)
