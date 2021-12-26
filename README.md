# Environment-Modeling-1
* Kodu çalıştırmanız için car2.mp4 videosu klasörün içinde olması lazım. Buradan indirebilirsiniz: https://github.com/mehmetserifpasa/Car-Object-Detection-Example-1

# Algorithm
Algoritmanın mantığı şu şekilde çalışır. 3x3 matrise karşılık gelen her pixelin çevre pixelleri kontrol edilir. Eğer 
ortadaki pixelin renk değeri (gri renk) ile her köşenin pixeli farkı 50'den büyükse şu çıkarıma varılır. Burada hızlı bir 
renk değişimi yaşanmış. Bundan yararlanılarak filitreleme işlemi yapılır. Aşşağıdaki görselde bu renk değişimine örnek
gösterebiliriz.

# Code
![Ekran Resmi 2021-12-27 01 38 01](https://user-images.githubusercontent.com/25556230/147421579-5e4bf91a-228e-4f4b-9886-add2ccb17006.png)
```
            LOCATION_LIST = [
                             self.location1, self.location2, self.location3,
                             self.location4, self.location5, self.location6,
                             self.location7, self.location8,
                             ]

            for lt in LOCATION_LIST:
                if(self.pixel[self.location9] - self.pixel[lt] > 50):
                    self.out.putpixel(
                        lt,
                        (255)
                    )
```
LOCATION_LIST, bizim 3x3 matrisin değerlerini tutar. Aşşağıda ise bu pixellerin her biri gezilerek fark değerlerine
bakılmış ve resimde değişiklik yapılmıştır. Kodda 50 sayısı ise bizim fark değerimiz. Bunda oynama yapılabilir fakat
uygunluk olarak ben bu sayıyı seçtim.

# Note
Bu algoritma tam bir şekilde kenarları algılamayabilir. Mesela çevre pixellerinin renk değeri ile kenar pixellerinin değeri
birbirine yakınsa bu algoritma tespit etmede zorlanabilir.

# Kaynaklar
1- https://en.wikipedia.org/wiki/Edge_detection
