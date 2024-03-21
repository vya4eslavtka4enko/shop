from django.shortcuts import render
from .models import Kids,Man,Woman,InSale
def main(request):
    inSaleData = InSale.objects.all()
    return render(request,'index.html',{'inSaleData':inSaleData})


def kids_clothes(request):
    kids_data = Kids.objects.all()
    return render(request,'kids_clothes.html',{'kids_data':kids_data})


def man(request):
    man = Man.objects.all()
    return render(request,'man_clothes.html',{'man':man})


def woman(request):
    woman = Woman.objects.all()
    return render(request,'woman_clothes.html',{'woman':woman})