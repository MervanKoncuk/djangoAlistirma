from django.contrib import admin
from .models import *

# Oluşturduğumuz modellerin admin panelinde görüntülenebilmesi için gereken komut
admin.site.register(Ogrenci)