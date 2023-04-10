from django.shortcuts import render

# Create your views here.
def show_about_us(request):
    return render(request,"about_us.html")

def show_catalog(request):
    return render(request,"catalog.html")
        
def show_main(request):
    return render(request,"main.html")
        
def show_support(request):
    return render(request,"support.html")
    