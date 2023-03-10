<h3>Adımlar : <h3/>
1 - django-admin startproject neosTicaret <br/>
2 - manage.py dosyasını çalıştırıp migrate komutunun girilmesi (veri tabanını oluşturmak için) <br/>
3 - manage.py startapp (app ismi) komutu ile app oluşturulması <br/>
--- admin paneline girebilmek için kullanıcı adı ve şifre oluşturma komutu : python manage.py createsuperuser --- <br/>
4 - settings.py dosyasında INSTALLED_APPS kısmına app ismi eklenmesi (appimizin projemizde çalışması için) - (virgülü unutmayın) <br/>
5 - html dosyalarımız için appimizin içerisine "templates" adında bir klasör oluşturulması <br/>
6 - css-image-js dosyalarımız için appimizin içerisine "static" adında bir klasör oluşturulması <br/>
7 - views.py dosyasında templates içerisine oluşturduğumuz html dosyalarını görüntüleyebilmek için gerekli fonksiyonların yazılması <br/>
8 - urls.py dosyasında appin içerisindeki views.py dosyasını import ettikten sonra oluşturduğumuz fonksiyonlar için gerekli path'lerin eklenmesi <br/>
9 - models.py içerisine veri tabanımız için tabloların oluşturulması <br/>
10 - eklenilen tabloların model haline getirilmesi için manage.py makemigrations komutunun girilmesi <br/>
11 - oluşturulan tabloların veri tabanına eklenmesi için manage.py migrate komutunun girilmesi <br/>
12 - admin.py dosyasına oluşturulan tabloların admin panelinde görüntülenebilmesi için gerekli komutların girilmesi (models.py import edilecek)
