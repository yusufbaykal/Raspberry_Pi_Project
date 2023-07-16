# KEDİM HEP YANIMDA


Bu proje, evcil hayvan besleyen bir bireyin hayvanın mama/su yediğini görüntülemeyi ve bu olayı tespit ettiğinde resim veya video çekerek kullanıcının mail adresine göndermeyi amaçlamaktadır. Bu sayede kullanıcı, evden uzakta olduğu durumlarda bile evcil hayvanının beslenmesini izleyebilir ve kontrol edebilir.

# Kullanılan Teknolojiler
* Python
* Sensörler
* Raspberry Pi
* Kamera
* SMTP protokolü

# Gereksinimler
Bu proje için aşağıdaki bileşenlere ihtiyaç vardır:

* Raspberry Pi (model 3B veya üstü önerilir)
* Raspberry Pi Kamera modülü
* PIR (Passive Infrared) hareket sensörü
* Breadboard
* Jumper kabloları
* WiFi bağlantısı
* Evcil hayvanın mama kabı ve su kabı

# Kullanım 

* #### Raspberry Pi'nin Kurulumunu:

Boş bir SD kart kullanarak Raspberry Pi için Raspbian işletim sistemini indirin ve SD kartınıza yazın.
Raspberry Pi'yi klavye, fare ve monitörle bağlayarak konfigürasyon ayarlarını yapın.
PuTTY gibi bir SSH istemcisini kullanarak Raspberry Pi'ye uzaktan erişim sağlamak için kişisel bilgisayarınıza bağlanın.

* #### Donanım Bağlantıları:

Jumper kabloları ve breadboard kullanarak PIR sensörü ile Raspberry Pi arasındaki bağlantıları yapın.
PIR sensörünü Raspberry Pi üzerindeki uygun GPIO pinine (örneğin GPIO 11) bağlayın.
Bağlantılar sırasında, jumper kablolarını Raspberry Pi ve breadboard üzerinde kısa devre olmayacak şekilde dikkatlice bağlayın.

* #### Python Programını Çalıştırın:

Raspberry Pi üzerinde bir terminal açın veya SSH istemcisini kullanarak Raspberry Pi'ye uzaktan erişim sağlayın.
Proje dosyalarının bulunduğu dizine gidin.
Terminalde, python main.py komutunu girerek Python programını başlatın.

* #### Sonuç:

Raspberry Pi, PIR sensöründen gelen hareketi izleyecek ve besleme olayını tespit ettiğinde işlemler gerçekleştirecektir.
PIR sensörü hareket algıladığında ve besleme tespit edildiğinde, kamera ile fotoğraf veya video çekilecektir.
Çekilen fotoğraf veya video, belirlediğiniz mail adresine SMTP protokolü kullanılarak gönderilecektir.

* #### Uygulama:
  https://drive.google.com/file/d/1oFSYlSMMvhqWkCX3J-IkE8zWjntEVMAg/view?usp=sharing
