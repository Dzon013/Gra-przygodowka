from Postacie import Przeciwnik
from Pasywne_Lokacje import Ekwipunek


class Gra:
    def __init__(self, koszt_levela):
        self.bohater = None
        self.przeciwnik1 = Przeciwnik("Armia Szkieletów", 300, 20, 100, 500)
        self.przeciwnik2 = Przeciwnik("Pająk gigant", 400, 40, 200, 600)
        self.przeciwnik3 = Przeciwnik("Zmutowana Mysz", 500, 60, 300, 700)
        self.przeciwnik4 = Przeciwnik("Kamienny Olbrzym", 600, 80, 400, 800)
        self.boss = Przeciwnik("Godzilla", 1000, 150, 1000, 1000)
        self.koszt_levela = koszt_levela

    def start(self, x):
        self.bohater = x
        print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
        self.poruszaj_sie()

    def poruszaj_sie(self):
        print("ZIEMIA")
        print("\nGdzie chcesz się udać?")
        print("1. Ścieżka niedoprzejścia")
        print("2. Jama")
        print("3. Bliskie spotkanie z....")
        print("4. Skalisty krater")
        print("5. Ognisko")
        print("6. Zbrojownia")
        print("7. Finałowy Boss")

        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            print("Uważaj na kości!")
            self.walka(self.przeciwnik1)
            self.poruszaj_sie()
        elif wybor == "2":
            print("Wchodzisz do jamy i spotykasz przeciwnika!")
            self.walka(self.przeciwnik2)
            self.poruszaj_sie()
        elif wybor == "3":
            print("...!")
            self.walka(self.przeciwnik3)
            self.poruszaj_sie()
        elif wybor == "4":
            print("Idziesz korytażem i spotykasz ogromny krater!")
            self.walka(self.przeciwnik4)
            self.poruszaj_sie()
        elif wybor == "5":
            regen = input("Odwiedzasz ognisko i regenerujesz zdrowie.\nTAK: Koszt: 10zł\nMAX: Koszt: 50zł\nNIE: aby wyjść:")
            if regen == "NIE":
                self.poruszaj_sie()
            elif regen == "TAK":
                self.bohater.zdrowie += 10
                self.bohater.pieniadze = self.bohater.pieniadze - 10
                print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                self.poruszaj_sie()
            elif regen == "MAX":
                self.bohater.zdrowie += 50
                self.bohater.pieniadze = self.bohater.pieniadze - 50
                print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                self.poruszaj_sie()
        elif wybor == "6":
            Ekwipunek.zbrojownia(self.bohater)
            print(f"5. Zwiększenie levela: Koszt: {self.koszt_levela}(+ 1 do level)")
            jeden = Ekwipunek("Exkalibur", 20, 200, 400)
            dwa = Ekwipunek("Kusza", 40, 400, 600)
            trzy = Ekwipunek("Pies", 200, 20, 300)
            cztery = Ekwipunek("Pancerz", 400, 40, 500)
            piec = Ekwipunek("Klucz", 0, 0, 500)

            kupno = input("Podaj liczbę: ")
            if kupno == "0":
                self.poruszaj_sie()
            elif kupno == "1":
                if self.bohater.pieniadze < jeden.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - jeden.cena
                    self.bohater.oslona = self.bohater.oslona + jeden.ochrona
                    self.bohater.sila = self.bohater.sila + jeden.atak
                    print("Zakupiono Exkalibur. Zadajesz teraz więcej obrażeń")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie()
            elif kupno == "2":
                if self.bohater.pieniadze < dwa.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - dwa.cena
                    self.bohater.oslona = self.bohater.oslona + dwa.ochrona
                    self.bohater.sila = self.bohater.sila + dwa.atak
                    print("Zakupiono kuszę. Zadajesz teraz jeszcze więcej obrażeń")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie()
                    self.poruszaj_sie()
            elif kupno == "3":
                if self.bohater.pieniadze < trzy.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - trzy.cena
                    self.bohater.oslona = self.bohater.oslona + trzy.ochrona
                    self.bohater.sila = self.bohater.sila + trzy.atak
                    print("Zakupiono Pieska. Możesz czuć się trochę bezpieczniej")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie()

            elif kupno == "4":
                if self.bohater.pieniadze < cztery.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - cztery.cena
                    self.bohater.oslona = self.bohater.oslona + cztery.ochrona
                    self.bohater.sila = self.bohater.sila + cztery.atak
                    print("Zakupiono Pancerz. Możesz czuć się ultra bezpieczny.")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie()
            elif kupno == "5":
                if self.bohater.pieniadze < piec.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - piec.cena
                    print("Zakupiono klucz. Zachowaj go na później.")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie()

            elif kupno == "5":
                self.koszt_levela = 50
                wzmocnienie = 20
                if self.bohater.pieniadze < self.koszt_levela:
                    print("Za mało pieniędzy")
                    self.poruszaj_sie()
                else:
                    while self.bohater.pieniadze >= self.koszt_levela:
                        self.bohater.pieniadze = self.bohater.pieniadze - self.koszt_levela
                        self.bohater.sila = self.bohater.sila + wzmocnienie
                        self.bohater.oslona = self.bohater.oslona + wzmocnienie
                        self.bohater.zdrowie = self.bohater.zdrowie + wzmocnienie
                        self.bohater.level = self.bohater.level + 1
                        wzmocnienie = wzmocnienie + 20
                        self.koszt_levela = self.koszt_levela + self.koszt_levela
                        print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                        self.poruszaj_sie()
        elif wybor == "7":
            print("Uwaga! Nadchodzi Finałowy BOSS!")
            self.walka(self.boss)
            if self.bohater.klucze == 1:
                self.bohater.klucze = self.bohater.klucze - 1
                print("Dziękujemy za grę")
                print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
            else:
                self.bohater.pieniadze = self.bohater.pieniadze + 200
                print("Zakup klucz!")
                brak = input("Jeśli nie masz pieniędzyna klucz wpisz `brak` \nw przeciwnym razie wpisz `mam`: ")
                if brak == "brak":
                    print("Przegrałeś :(")
                elif brak == "mam":
                    print("Idź go kup!!!")
                    self.poruszaj_sie()
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            self.poruszaj_sie()

    def walka(self, przeciwnik):
        while self.bohater.zdrowie > 0 and przeciwnik.zdrowie > 0:
            print("\n1. Atak")
            print("2. Ucieczka")
            wybor = input("Wybierz opcję: ")
            if wybor == "1":
                self.bohater.atakuj(przeciwnik)
                if przeciwnik.zdrowie > 0:
                    przeciwnik.atakuj(self.bohater)
            elif wybor == "2":
                print("Uciekasz z walki!")
                self.bohater.pieniadze = self.bohater.pieniadze - 10
                przeciwnik.zdrowie = przeciwnik.zdrowie + 50
                self.poruszaj_sie()
                break
            else:
                print("Nieprawidłowy wybór.")
        if self.bohater.oslona <= 0:
            if self.bohater.zdrowie <= 0:
                print("Przegrałeś! Gra zakończona.")
        elif przeciwnik.zdrowie <= 0:
            print(f"Wygrałeś walkę!\n otrzymujesz {przeciwnik.xp} punktów oraz {przeciwnik.xp}zł")
            self.bohater.punkty = self.bohater.punkty + przeciwnik.xp
            self.bohater.pieniadze = self.bohater.pieniadze + przeciwnik.xp
            print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
            self.poruszaj_sie()

