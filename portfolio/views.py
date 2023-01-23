from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from portfolio.forms import Form_contact
# Create your views here.


def home(request):
    projects = Project.objects.all()

    return render(request, 'home.html', {'projects': projects})

def contact(request):

    if request.method=="POST":

        subject = request.POST["asunto"]

        message = request.POST["mensaje"] + " " + request.POST["email"]

        email_from = settings.EMAIL_HOST_USER

        recipient_list = ["arathgg143@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")

    return render(request, 'contact.html')


# def contact(request):

#     if request.method == "POST":

#         miFormulario = Form_contact(request.POST)

#         if miFormulario.is_valid():

#             infForm = miFormulario.cleaned_data

#             send_mail(infForm['asunto'], infForm['mensaje'],
#                       infForm.get('email', ''), ['arathgg143@gmail.com'],)

#             return render(request, "gracias.html")

#     else:

#         miFormulario = Form_contact()

#     return render(request, "form_contact.html", {"form": miFormulario})

    # projects = Project.objects.all()

    # return render(request, 'contact.html',{'projects':projects})
