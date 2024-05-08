class SahmatFiquru:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def move(self):
        pass

    def __str__(self):
        return f"{self.color} {self.__class__.__name__} at {self.position}"

class Sah(SahmatFiquru):
    def move(self):
        return "1 xana hər istiqamətə hərəkət edə bilər."

class Vezir(SahmatFiquru):
    def move(self):
        return "İstənilən sayda xana vertikal, horizontal və diaqonal hərəkət edə bilər."

class At(SahmatFiquru):
    def move(self):
        return "L şəklində hərəkət edə bilər: iki xana düz və bir yan."


sah = Sah("Ağ", "E1")
vezir = Vezir("Qara", "D8")
at = At("Ağ", "B1")


figurlar = [sah, vezir, at]
for fig in figurlar:
    print(fig)
    print(fig.move())


