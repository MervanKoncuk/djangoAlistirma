from django.db import models

# Model = Veri tabanı tablosu
# tablo oluşturma komutu : makemigrations
# oluşturulan tabloyu veri tabanına ekleme komutu : migrate

class Ogrenci(models.Model):
    isim = models.CharField(max_length=100) # type text
    aciklama = models.TextField(max_length=300) # textarea
    numara = models.IntegerField() # type number

    def __str__(self):
        return self.isim