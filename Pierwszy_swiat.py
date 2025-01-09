from Postacie import Przeciwnik
from Postacie import Bohater
from Pasywne_Lokacje import Ekwipunek
import Drugi_swiat


class Gra:
    def __init__(self, koszt_levela):
        self.bron = None
        self.bohater = None
        self.przeciwnik1 = Przeciwnik("Goblin", 30, 5, 50, 50)
        self.przeciwnik2 = Przeciwnik("Pająk", 50, 15, 100, 100)
        self.przeciwnik3 = Przeciwnik("Śmierć", 70, 30, 200, 200)
        self.przeciwnik4 = Przeciwnik("Terroryści", 100, 20, 300, 300)
        self.boss = Przeciwnik("Smok", 300, 40, 400, 400)
        self.koszt_levela = koszt_levela

    def start(self):
        print("Witaj w grze przygodowej!")
        imie = input("Jaki masz pseudonim, bohaterze?\n")
        if imie == "admin":
            haslo1 = input("Podaj hasło: ")
            if haslo1 == "1234":
                self.bohater = Bohater(imie, 1000, 1000, 100000, 10000, 100000, 999, 2)
                print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                self.poruszaj_sie()
            else:
                print("nieprawidłowe hasło\nOdpal grę ponownie")
        else:
            self.bohater = Bohater(imie, 10, 10, 0, 100, 0, 0, 0)
            print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
            self.poruszaj_sie()

    def poruszaj_sie(self):
        print("\nZIEMIA")
        print("Gdzie chcesz się udać?")
        print("1. Las")
        print("2. jaskinia")
        print("3. Bliskie spotkanie z....")
        print("4. konwuj bandziorów")
        print("5. Wioska")
        print("6. Zbrojownia")
        print("7. Boss")
        print("8. Drugi Świat")

        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            print("Wchodzisz do lasu i spotykasz przeciwnika!")
            self.walka(self.przeciwnik1)
            self.poruszaj_sie()
        elif wybor == "2":
            print("Wchodzisz do jaskini i spotykasz przeciwnika!")
            self.walka(self.przeciwnik2)
            self.poruszaj_sie()
        elif wybor == "3":
            print("Wstąpiłeś na cmentarz!")
            self.walka(self.przeciwnik3)
            self.poruszaj_sie()
        elif wybor == "4":
            print("Idziesz ulicą i spotykasz konwuj terrorystów!")
            self.walka(self.przeciwnik4)
            self.poruszaj_sie()
        elif wybor == "5":
            regen = input("Odwiedzasz wioskę i regenerujesz zdrowie.\nTAK: Koszt: 10zł\nMAX: Koszt: 50zł\nNIE: aby wyjść:")
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
            Ekwipunek.zbrojownia(self.bron)
            print(f"5. Zwiększenie levela: Koszt: {self.koszt_levela}(+ 1 do level)")
            print("6. Klucz: koszt: 500zł (???)")
            jeden = Ekwipunek("miecz", 10, 30, 120)
            dwa = Ekwipunek("Łuk", 15, 100, 200)
            trzy = Ekwipunek("Tarcza", 40, 10, 150)
            cztery = Ekwipunek("Zbroja", 100, 20, 300)
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
                    print("Zakupiono miecz. Zadajesz teraz więcej obrażeń")
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
                    print("Zakupiono łuk. Zadajesz teraz jeszcze więcej obrażeń")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie()
            elif kupno == "3":
                if self.bohater.pieniadze < trzy.cena:
                    print("Za mało punktów")
                    self.poruszaj_sie()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - trzy.cena
                    self.bohater.oslona = self.bohater.oslona + trzy.ochrona
                    self.bohater.sila = self.bohater.sila + trzy.atak
                    print("Zakupiono tarczę. Możesz czuć się trochę bezpieczniej")
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
                    print("Zakupiono zbroję. Możesz czuć się ultra bezpieczny.")
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
                        wzmocnienie = wzmocnienie + wzmocnienie
                        self.bohater.sila = self.bohater.sila + wzmocnienie
                        self.bohater.oslona = self.bohater.oslona + wzmocnienie
                        self.bohater.zdrowie = self.bohater.zdrowie + wzmocnienie
                        self.bohater.level = self.bohater.level + 1
                        print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                        self.poruszaj_sie()
            elif kupno == "6":
                if self.bohater.pieniadze < piec.cena:
                    print("Za mało pieniędzy")
                    self.poruszaj_sie()
                else:
                    self.bohater.pieniadze = self.bohater.pieniadze - piec.cena
                    self.bohater.klucze = self.bohater.klucze + 1
                    print("Zakupiono klucz. Zachowaj go na później.")
                    print(f"STATYSTYKI:\npseudonim: {self.bohater.imie}\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel: {self.bohater.level}\nKlucze: {self.bohater.klucze}")
                    self.poruszaj_sie()
        elif wybor == "7":
            print("Uwaga! Nadchodzi BOSS!")
            self.walka(self.boss)
        elif wybor == "8":
            if self.bohater.punkty >= 1000:
                if self.bohater.klucze >= 1:
                    koniec_1 = input("Ukończyłeś 1 świat !!!\nJeśli chcesz grać dalej wpisz `dalej`\nJeśli chcesz wrócić do pierwszego wpisz `koniec`\n")
                    if koniec_1 == "dalej":
                        self.bohater.klucze = self.bohater.klucze - 1
                        x = Bohater(self.bohater.imie, self.bohater.zdrowie, self.bohater.sila, self.bohater.punkty, self.bohater.pieniadze, self.bohater.oslona, self.bohater.level, self.bohater.klucze)
                        swiat2 = Drugi_swiat.Gra(50)
                        swiat2.start(x)
                    elif koniec_1 == "koniec":
                        self.poruszaj_sie()
                    else:
                        print("Nieprawidłowy wybór")
                        self.poruszaj_sie()
                else:
                    print("Brakuje klucza")
                    self.poruszaj_sie()
            else:
                print("Za mało punktów")
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

