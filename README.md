Adımlar : 
1 - django-admin startproject neosTicaret
2 - manage.py dosyasını çalıştırıp migrate komutunun girilmesi (veri tabanını oluşturmak için)
3 - manage.py startapp (app ismi) komutu ile app oluşturulması 
--- admin paneline girebilmek için kullanıcı adı ve şifre oluşturma komutu : python manage.py createsuperuser ---
4 - settings.py dosyasında INSTALLED_APPS kısmına app ismi eklenmesi (appimizin projemizde çalışması için) - (virgülü unutmayın)
5 - html dosyalarımız için appimizin içerisine "templates" adında bir klasör oluşturulması
6 - css-image-js dosyalarımız için appimizin içerisine "static" adında bir klasör oluşturulması
7 - views.py dosyasında templates içerisine oluşturduğumuz html dosyalarını görüntüleyebilmek için gerekli fonksiyonların yazılması
8 - urls.py dosyasında appin içerisindeki views.py dosyasını import ettikten sonra oluşturduğumuz fonksiyonlar için gerekli path'lerin eklenmesi
9 - models.py içerisine veri tabanımız için tabloların oluşturulması
10 - eklenilen tabloların model haline getirilmesi için manage.py makemigrations komutunun girilmesi
11 - oluşturulan tabloların veri tabanına eklenmesi için manage.py migrate komutunun girilmesi
12 - admin.py dosyasına oluşturulan tabloların admin panelinde görüntülenebilmesi için gerekli komutların girilmesi (models.py import edilecek)
