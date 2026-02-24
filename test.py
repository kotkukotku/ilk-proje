class Bera:
    def __init__(self,ad,soyad,sinifno):
        self.cinselyonelim = "Gey" 
        self.ad = ad
        self.soyad = soyad
        self.sinifno = sinifno
        self.domaldi_mi = True
    def __str__(self):
        return f"Cinsel Yönelimi: {self.cinselyonelim}\nAdı:{self.ad}\nSoyadı:{self.soyad}\n" \
        f"Sınıf No:{self.sinifno}\nDomaldı Mı:{self.domaldi_mi}"
    
bera1 = Bera("Bera","Elsa",1453)
bera2 = Bera("Bera","Vazektomizt",571)

