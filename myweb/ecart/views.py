from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    # print(products[0])
    # for i in products:
    #      print(i.desc)

    allprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nslides),nslides])

    #print(nslparams = {"product": products,"no_of_slides":nslides,"range":range(nslides)}
    # allprods = [[prod,range(1,nslides),nslides],
    #              [prod,range(1,nslides),nslides]]
    params = {'allprods':allprods}
    return render(request,'ecart/index.html',params)




#
# def index(request):
#     # products = Product.objects.all()
#     # print(products)
#     # n = len(products)
#     # nSlides = n//4 + ceil((n/4)-(n//4))
#
#     allProds = []
#     catprods = Product.objects.values('category', 'id')
#     cats = {item['category'] for item in catprods}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(prod)
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         allProds.append([prod, range(1, nSlides), nSlides])
#
#     # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
#     # allProds = [[products, range(1, nSlides), nSlides],
#     #             [products, range(1, nSlides), nSlides]]
#     params = {'allProds':allProds}
#     return render(request, 'shop/index.html', params)


def about(request):
    return render(request,'ecart/about.html')

def contact(request):
    return HttpResponse("This is contact page")

def tracker(request):
    return HttpResponse("This is tracker page")

def search(request):
    return HttpResponse("This is search page")


def productlist(request):
    return HttpResponse("This is product page")

def checkout(request):
    return HttpResponse("This is checkout page")