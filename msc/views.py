from django.shortcuts import render
from django.http import HttpResponse
from .models import product, contact
from math import ceil

# Create your views here.

def viewsfnc(request):
    products= product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"msc/mschome.html", params)


def about(request):
    return render(request, 'msc/about.html')

def contacts(request):
    if request.method == "POST":
        # form = request.POST.get('form', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phno = request.POST.get('phno', '')
        des = request.POST.get('des', '')
        print(name, email, phno, des)
        Contact = contact(name=name, email=email, phno=phno, des=des)
        Contact.save()
    return render(request, 'msc/contact.html')

def tracker(request):
    return render(request, 'msc/tracker.html')

def productview(request, id):
    # produ = product.objects.all()
    products = product.objects.filter(id=id)
    dicti = {'product':products[0]}
    return render(request, 'msc/productview.html', dicti)

def search(request):
    return render(request, 'msc/search.html')

def checkout(request):
    return render(request, 'msc/checkout.html')