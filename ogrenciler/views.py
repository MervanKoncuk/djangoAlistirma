from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    ogrenciler = Ogrenci.objects.all()
    # print(ogrenciler)
    # sozluk = {
    #     'isimler':['Ali', 'Çağla', 'Elif'],
    # }
    # print(sozluk)
    # for i in sozluk['isimler']:
    #     print(i)
    context = {
        'ogr':ogrenciler
    }
    return render(request, 'index.html', context)


def hakkimizda(request):
    return render(request, 'hakkimizda.html')


def detail(request, ogrenciId):
    # get fonksiyonu ile tek bir obje çekilir.
    # filter fonksiyonu ile birden fazla obje çekilir.
    ogrenci = Ogrenci.objects.get(id = ogrenciId)
    print(ogrenci)
    context = {
        'ogrenci':ogrenci
    }
    return render(request, 'detail.html', context)