from django.shortcuts import render
from shop_cookies_app.models import *
# Create your views here.
def show_catalog(request):
    response = render(request, "catalog.html", context={'products': Product.objects.all()})
    
    if request.method == "POST": 
        # product_count = request.POST.get("product_count")
        # product_count = int(product_count)
        # for i in range(product_count):
            if "product_pk" not in request.COOKIES: 
                product = request.POST.get('product_pk')
                response.set_cookie('product_pk', product)
                # return response
            else:
                product = request.COOKIES['product_pk'] + ' ' + request.POST.get('product_pk')  
                response.set_cookie('product_pk', product)
        # return response

    return response

def show_cart(request):
    if 'product_pk' in request.COOKIES:
        products_pk = request.COOKIES['product_pk']
        products_pk = products_pk.split(' ')

        list_products = list()

        for product_pk in products_pk:
            list_products.append(Product.objects.get(pk=product_pk))

        response = render(request , 'basket.html', context={'products': list_products})

    else:
        response = render(request , 'basket.html', context={'products': list()})

    if request.method == 'POST':
        product_pk_choosed = request.POST.get("product_pk")
        try: 
            if len(products_pk) >= 2:
                products_pk.remove(f"{product_pk_choosed}")
                delete_product = " ".join(products_pk)
                response.set_cookie("product_pk", delete_product)
                return response
            else:
                response.delete_cookie("product_pk")
                return response
        except: 
            print()
    return response