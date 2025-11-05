class karaktär:
    def __init__(self, namn, hälsa, attack_kraft):
        self.namn = namn
        self._hälsa = hälsa
        self.attack_kraft = attack_kraft
     
    def is_alive(self):
        return self._hälsa > 0
    
    def get_health(self):
        return self._hälsa
    
    def take_damage(self, amount):
        self._hälsa = max(self._hälsa - amount, 0)
        print(f"{self.namn} tar {amount} skada. Hälsa kvar: {self._hälsa}")

    def attack(self, other):
        print(f"{self.namn} gör vanlig attack mot {other.namn} och gör {self.attack_kraft} skada.")
        other.take_damage(self.attack_kraft)
    
    def special(self, other):
        self.attack(other)

    def resurs_text(self):
        return ""

class Mage(karaktär):
    def __init__(self, namn, hälsa, attack_kraft, mana):
        super().__init__(namn, hälsa, attack_kraft)
        self.mana = mana
        self.special_namn = "Eldkot"

    def attack(self, other):
        skada = self.attack_kraft + 2
        print(f"{self.namn} använder magiskt attack mot {other.namn}  för {skada} skada")
        other.take_damage(skada)

    def special(self, other):
        kostnad = 3
        if self.mana >= kostnad:
            self.mana -= kostnad
            skada = self.attack_kraft + 10
            print(f"{self.namn} använder specialattack {self.special_namn} ({kostnad} mana) och gör {skada} skada!")
            other.take_damage(skada)
        else:
            print(f"{self.namn} har inte tillräckligt med mana för {self.special_namn}. Utför vanlig attack istället.")
            self.attack(other)

    def resurs_text(self):
        return f"Mana: {self.mana}"
    
class Ranger(karaktär):
    def __init__(self, namn, hälsa, attack_kraft, energy):
        super().__init__(namn, hälsa, attack_kraft)
        self.energy = energy
        self.special_namn = "Snabbskott"

    def attack(self, other):
        skada = self.attack_kraft + 1
        print(f"{self.namn} skjuter pil mot {other.namn} för {skada} skada")
        other.take_damage(skada)
    
    def special(self, other):
        kostnad = 2
        if self.energy >= kostnad:
            self.energy -= kostnad
            skada = self.attack_kraft + 6
            print(f"{self.namn} använder specialattack {self.special_namn} ({kostnad} energy) och gör {skada} skada!")
            other.take_damage(skada)
        else:
            print(f"{self.namn} har inte tillräckligt med energy för {self.special_namn}. Utför vanlig attack istället.")
            self.attack(other)

    def resurs_text(self):
        return f"Energy: {self.energy}"

class Warrior(karaktär):
    def __init__(self, namn, hälsa, attack_kraft, stamina):
        super().__init__(namn, hälsa, attack_kraft)
        self.stamina = stamina
        self.special_namn = "Berserkerslag"
   
    def attack(self, other):
        skada = self.attack_kraft + 3
        print(f"{self.namn} slår hårt och gör {skada} skada på {other.namn}.")
        other.take_damage(skada)

    def special(self, other):
        kostnad = 2
        if self.stamina >= kostnad:
            self.stamina -= kostnad
            skada = self.attack_kraft + 8
            print(f"{self.namn} använder specialattack {self.special_namn} ({kostnad} stamina) och gör {skada} skada.")
            other.take_damage(skada)
        else:
            print(f"{self.namn} har inte tillräckligt med stamina för {self.special_namn}. Utför vanlig attack istället.")
            self.attack(other)

    def resurs_text(self):
        return f"Stamina: {self.stamina}"

class Arena:
    def __init__(self, spelare, motståndare):
        self.spelare = spelare
        self.motståndare = motståndare

    def start_fight(self):
        tur_spelare = True
        runda = 1
        print(f"\nStriden börjar: {self.spelare.namn} vs {self.motståndare.namn}\n")
        while self.spelare.is_alive() and self.motståndare.is_alive():
            print(f"Runda: {runda}")
            if tur_spelare:
                print(f"Din tur: {self.spelare.namn}")
                print(f"Din hälsa: {self.spelare.get_health()}  Motståndarens hälsa: {self.motståndare.get_health()}")
                print("1) Använd vanlig attack")

                text = self.spelare.resurs_text()
                if text:
                   print(f"2) Använd specialattack  ({text})")
                else:
                  print("2) Använd specialattack (ingen extra resurs)")
                val = input("Välj (1-2): ")
                if val == "2":
                    self.spelare.special(self.motståndare)
                else:
                    self.spelare.attack(self.motståndare)
            else:
                print(f"Motståndarens tur: {self.motståndare.namn}")
                self.motståndare.special(self.spelare)

            tur_spelare = not tur_spelare
            runda += 1
            print("")
        if self.spelare.is_alive():
            print(f"Slutresultat: {self.spelare.namn} vinner striden!")
        else:
            print(f"Slutresultat: {self.motståndare.namn} vinner striden!")


def start_spel():
    print("Välj din karaktär:")
    print("1) Robin (Ranger)")
    print("2) Merlin (Mage)")
    print("3) Thor (Warrior)")
    val = input("Ditt val (1-3): ")

    if val == "1":
        spelare = Ranger("Robin", 100, 4, energy=15)
        motståndare = Warrior("Thor", 100, 2, stamina=20)
    elif val == "2":
        spelare = Mage("Merlin", 100, 3, mana=18)
        motståndare = Ranger("Robin", 100, 4, energy=15)
    else:
        spelare = Warrior("Thor", 100, 2, stamina=20)
        motståndare = Mage("Merlin", 100, 3, mana=18)

    arena = Arena(spelare, motståndare)
    arena.start_fight()


if __name__ == "__main__":
    start_spel()



