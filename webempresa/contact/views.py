from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    #print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviamos el correo y direccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["1922c234dc-fbb103+1@inbox.mailtrap.io"],
                reply_to=[email]
            )

            try:
                email.send()
                #Todo ha ido mal redireccionamos a ok
                return redirect(reverse ('contact')+"?ok")
            except:
                #Algo no ha ido bien redireccionamos a fail
                return redirect(reverse ('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})