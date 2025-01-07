class Ekwipunek:
    def __init__(self, bron, ochrona, atak, cena):
        self.bohater = None
        self.ochrona = ochrona
        self.atak = atak
        self.cena = cena
        self.bron = bron

    def zbrojownia(self):
        print("Witamy w zbrojowni. Co chciałbyś kupić?: ")
        print("0. Nic")
        print("1. Miecz: 120zł (+30 do obrażeń)")
        print("2. Łuk: 200zł (+100 do obrażeń)")
        print("3. Tarcza: 150zł (+ 25 do osłony)")
        print("4. Zbroja: 300zł (+ 100 do osłony)")


