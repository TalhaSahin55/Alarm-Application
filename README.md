# Alarm Uygulaması

Kendimi geliştirmek amacıyla yaptığım projemde "datetime", "pygame" ve "time" kütüphanelerini 
kullandığım Python dilinde yazılmış Alarm Uygulaması'nı incelediğiniz için teşekkür ederim.

## Proje Kurulumu
```
python -m venv env
source env/bin/activate
pip install pygame
pip install time
pip install datetime
```

## Proje Açıklaması
  
- Proje saat, dakika ve saniyeyi girebildiğiniz bir alarm sistemi olacak.
- Alarm tekrar sayısı girilebilecek.
- Saat sisteminde aykırı sayıların girilmesi engellenecek.
- Alarm tekrar sisteminde aykırı sayıların girilmesi engellenecek.
  
## Projedeki Eksikler
Projede geliştirilebilecek birçok şey var bunları farkettiğim ve geliştirilmesi gereken şeyleri listeledim.
  
- Kullanıcıya alarm sesi listesi sunup, alarm sesini kullanıcının insiyatifine bırakılabilir.
- Alarm zamanı geldiğinde alarm sesi dışında görsel bir uyarı ekranı açılabilir.
