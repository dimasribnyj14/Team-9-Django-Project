from django.shortcuts import render
from MovieApp.models import *
from django.core.mail import send_mail
from MovieStore.settings import EMAIL_HOST_USER

# Create your views here.
def show_index(request):
    context = {
        "movies":Movie.objects.all()
    }
    if request.method == "POST":
        subject = "Відгук"
        name = request.POST.get("nameClient")
        message_client = request.POST.get("message")
        message = "Клієнт " + name + " Залишив свій відгук: "+ message_client 
        Message.objects.create(name = name, message = message_client, email = EMAIL_HOST_USER)
        send_mail(subject = subject, message = message, from_email = "settings.EMAIL_HOST_USER", recipient_list = [EMAIL_HOST_USER], fail_silently = False)
    return render(request, "index.html", context)

