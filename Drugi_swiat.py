from Postacie import Przeciwnik
from Postacie import Bohater
from Pasywne_Lokacje import Ekwipunek
import Pierwszy_swiat



class Gra:
    def __init__(self, koszt_levela, wzmocnienie):
        self.bron = None
        self.bohater = None
        self.przeciwnik1 = Przeciwnik("Armia Szkieletów", 300, 20, 100, 500)
        self.przeciwnik2 = Przeciwnik("Pająk gigant", 400, 40, 200, 600)
        self.przeciwnik3 = Przeciwnik("Zmutowana Mysz", 500, 60, 300, 700)
        self.przeciwnik4 = Przeciwnik("Kamienny Olbrzym", 600, 80, 400, 800)
        self.boss = Przeciwnik("Godzilla", 1000, 150, 1000, 1000)
        self.koszt_levela = koszt_levela
        self.wzmocnienie = wzmocnienie

    def start(self, x):
        self.bohater = x
        print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
        self.poruszaj_sie2()

    def poruszaj_sie2(self):
        print("PODZIEMIA")
        print("\nGdzie chcesz się udać?")
        print("1. Ścieżka niedoprzejścia")
        print("2. Jama")
        print("3. Bliskie spotkanie z....")
        print("4. Skalisty krater")
        print("5. Ognisko")
        print("6. Zbrojownia")
        print("7. Finałowy Boss")
        print("8. Koniec Gry")

        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            print("Uważaj na kości!")
            self.walka(self.przeciwnik1)
        elif wybor == "2":
            print("Wchodzisz do jamy i spotykasz przeciwnika!")
            self.walka(self.przeciwnik2)
        elif wybor == "3":
            print("...!")
            self.walka(self.przeciwnik3)
        elif wybor == "4":
            print("Idziesz korytażem i spotykasz ogromny krater!")
            self.walka(self.przeciwnik4)
        elif wybor == "5":
            regen = input("Odwiedzasz ognisko i regenerujesz zdrowie.\nTAK: Koszt: 20zł\nMAX: Koszt: 100zł\nNIE: aby wyjść:")
            if regen == "NIE":
                self.poruszaj_sie2()
            elif regen == "TAK":
                self.bohater.zdrowie += 20
                self.bohater.pieniadze = self.bohater.pieniadze - 20
                print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                self.poruszaj_sie2()
            elif regen == "MAX":
                self.bohater.zdrowie += 100
                self.bohater.pieniadze = self.bohater.pieniadze - 100
                print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                self.poruszaj_sie2()
        elif wybor == "6":
            Ekwipunek.zbrojownia(self.bron)
            print(f"5. Zwiększenie levela: Koszt: {self.koszt_levela}(+ 1 do level)")
            print("6. Klucz: koszt: 1000zł (???)")
            jeden = Ekwipunek("Exkalibur", 20, 200, 400)
            dwa = Ekwipunek("Kusza", 40, 400, 600)
            trzy = Ekwipunek("Pies", 200, 20, 300)
            cztery = Ekwipunek("Pancerz", 400, 40, 500)
            piec = Ekwipunek("Klucz", 0, 0, 1000)

            kupno = input("Podaj liczbę: ")
            if kupno == "0":
                self.poruszaj_sie2()
            elif kupno == "1":
                if self.bohater.pieniadze < jeden.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie2()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - jeden.cena
                    self.bohater.oslona = self.bohater.oslona + jeden.ochrona
                    self.bohater.sila = self.bohater.sila + jeden.atak
                    print("Zakupiono Exkalibur. Zadajesz teraz więcej obrażeń")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie2()
            elif kupno == "2":
                if self.bohater.pieniadze < dwa.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie2()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - dwa.cena
                    self.bohater.oslona = self.bohater.oslona + dwa.ochrona
                    self.bohater.sila = self.bohater.sila + dwa.atak
                    print("Zakupiono kuszę. Zadajesz teraz jeszcze więcej obrażeń")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie2()
            elif kupno == "3":
                if self.bohater.pieniadze < trzy.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie2()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - trzy.cena
                    self.bohater.oslona = self.bohater.oslona + trzy.ochrona
                    self.bohater.sila = self.bohater.sila + trzy.atak
                    print("Zakupiono Pieska. Możesz czuć się trochę bezpieczniej")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie2()

            elif kupno == "4":
                if self.bohater.pieniadze < cztery.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie2()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - cztery.cena
                    self.bohater.oslona = self.bohater.oslona + cztery.ochrona
                    self.bohater.sila = self.bohater.sila + cztery.atak
                    print("Zakupiono Pancerz. Możesz czuć się ultra bezpieczny.")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie2()

            elif kupno == "5":
                self.koszt_levela += 50
                self.wzmocnienie += 20
                if self.bohater.pieniadze < self.koszt_levela:
                    print("Za mało pieniędzy")
                    self.poruszaj_sie2()
                else:
                    while self.bohater.pieniadze >= self.koszt_levela:
                        self.bohater.pieniadze = self.bohater.pieniadze - self.koszt_levela
                        self.bohater.sila = self.bohater.sila + self.wzmocnienie
                        self.bohater.oslona = self.bohater.oslona + self.wzmocnienie
                        self.bohater.zdrowie = self.bohater.zdrowie + self.wzmocnienie
                        self.bohater.level = self.bohater.level + 1
                        print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                        self.poruszaj_sie2()

            elif kupno == "6":
                if self.bohater.pieniadze < piec.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie2()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - piec.cena
                    self.bohater.klucze = self.bohater.klucze + 1
                    print("Zakupiono klucz. Zachowaj go na później.")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie2()

            else:
                print("nieprawidłowy wybór")
                self.poruszaj_sie2()
        elif wybor == "7":
            print("Uwaga! Nadchodzi Finałowy BOSS!")
            self.walka(self.boss)

        elif wybor == "8":
            if self.bohater.punkty >= 3000:
                if self.bohater.klucze >= 1:
                    koniec_1 = input("Ukończyłeś 2 świat !!!\nJeśli chcesz skończyć wpisz `koniec`\nJeśli chcesz wrócić wpisz `dalej`\n")
                    if koniec_1 == "koniec":
                        self.bohater.klucze = self.bohater.klucze - 1
                        print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                        print("Dziękujemy za grę")

                    elif koniec_1 == "dalej":
                        self.poruszaj_sie2()
                    else:
                        print("Nieprawidłowy wybór")
                        self.poruszaj_sie2()
                else:
                    print("Brakuje klucza")
                    self.poruszaj_sie2()
            else:
                print("Za mało punktów")
                self.poruszaj_sie2()
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            self.poruszaj_sie2()

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
                self.bohater.pieniadze -= 100
                przeciwnik.zdrowie += 500
                self.poruszaj_sie2()
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
            self.poruszaj_sie2()

