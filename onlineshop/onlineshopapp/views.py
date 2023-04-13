from django.shortcuts import render, redirect
from onlineshopapp.models import *
from django.core.mail import send_mail
from onlineshop.settings import EMAIL_HOST_USER

# Create your views here.
def show_about_us(request):
    return render(request,"about_us.html")

def show_catalog(request):
    context = {
        "Camera": Product.objects.filter(category__name = "Camera"),
        "Monitor": Product.objects.filter(category__name = "Monitor"),
        "Product": Product.objects.all(),
    }
    if request.method == "POST":
        category_name = request.POST.get("categoryChange")
        if category_name != "Усі":
            context.update({"Product": Product.objects.filter(category__name = category_name)})
        else:
            context.update({"Product": Product.objects.all()})
        # return redirect("catalog")
    return render(request,"catalog.html", context = context)
        
def show_main(request):
    return render(request,"main.html")
        
def show_support(request):
    if request.method == "POST":
        subject = "Відгук"
        name = request.POST.get("nameClient")
        message_client = request.POST.get("message")
        message = "Клієнт "+ name + " залишив свій відгук: " + message_client
        Message.objects.create(name = name, message = message, email = EMAIL_HOST_USER)
        send_mail(subject = subject, message = message, from_email = "settings.EMAIL_HOST_USER", recipient_list = [EMAIL_HOST_USER], fail_silently = False)
    return render(request,"support.html")
    