
from django.test import TestCase
from .models import Ogrenci

class OgrenciTest(TestCase):
    def test_ogrenci_olusturma(self):
        ogrenci = Ogrenci.objects.create(isim='Ahmet', aciklama='Öğrenci 1', numara='12345')
        # Oluşturulan öğrencinin bilgileri ve alanları uyuşuyor mu diye kontrol ediliyor
        self.assertEqual(ogrenci.isim, 'Ahmet')
        self.assertEqual(ogrenci.aciklama, 'Öğrenci 1')
        self.assertEqual(ogrenci.numara, '12345')
