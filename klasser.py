class karaktär:
    def __init__(self, namn, hälsa, attackkraft):
        self.namn = namn
        self._hälsa = hälsa
        self.attackkraft = attackkraft
     
    def is_alive(self):
        return self._hälsa > 0
    
    def get_health(self):
        return self._hälsa
    
    def take_damage(self, amount):
        self._hälsa = max(self._hälsa - amount, 0)
        print(f"{self.namn} tar {amount} skada. Hälsa kvar: {self._hälsa}")

    def attack(self, other):
        print(f"{self.namn} attackerar {other.namn} för {self.attackkraft} skada")
        other.take_damage(self.attackkraft)

class Mage(karaktär):
    def __init__(self, namn, hälsa, attackkraft, mana):
        super().__init__(namn, hälsa, attackkraft)
        self.mana = mana

    def attack(self, other):
        damage = self.attackkraft + 2
        print(f"{self.namn} använder magiskt attack mot {other.namn}  för {damage} skada")
        other.take_damage(damage)

    def special(self, other):
        if self.mana >= 3:
            self.mana -= 3
            skada = self.attackkraft + 6
            print(f"{self.namn} använder special (mana kvar {self.mana}) för {skada} skada.")
            other.take_damage(skada)
        else:
            print(f"{self.namn} har inte tillräckligt med mana. Utför vanlig attack istället.")
            self.attack(other)

class Ranger(karaktär):
    def __init__(self, namn, hälsa, attackkraft, energy):
        super().__init__(namn, hälsa, attackkraft)
        self.energy = energy

    def attack(self, other):
        damage = self.attackkraft + 1
        print(f"{self.namn} skjuter pil mot {other.namn} för {damage} skada")
        other.take_damage(damage)
    
    def special(self, other):
        if self.energy >= 2:
            self.energy -= 2
            skada = self.attackkraft + 4
            print(f"{self.namn} använder special (energy kvar {self.energy}) för {skada} skada.")
            other.take_damage(skada)
        else:
            print(f"{self.namn} har inte tillräckligt med energy. Utför vanlig attack istället.")
            self.attack(other)

class Warrior(karaktär):
    def __init__(self, namn, hälsa, attackkraft, stamina):
        super().__init__(namn, hälsa, attackkraft)
        self.stamina = stamina
   
    def attack(self, other):
        damage = self.attackkraft + 3
        print(f"{self.namn} svingar svärd mot {other.namn} för {damage} skada")
        other.take_damage(damage)

    def special(self, other):
        if self.stamina >= 2:
            self.stamina -= 2
            skada = self.attack_power + 5
            print(f"{self.namn} använder special (stamina kvar {self.stamina}) för {skada} skada.")
            other.take_damage(skada)
        else:
            print(f"{self.namn} har inte tillräckligt med stamina. Utför vanlig attack istället.")
            self.attack(other)

class Arena:
    def __init__(self, spelare1, spelare2):
        self.spelare1 = spelare1
        self.spelare2 = spelare2

    def fight(self):
        attacker = self.spelare1
        defender = self.spelare2
        runda = 1
        while attacker.is_alive() and defender.is_alive():
            print(f"\nRunda {runda}")

mage = Mage("Merlin", 20, 3, mana = 10)
ranger = Ranger("Robin", 18, 4, energy = 8)
warrior = Warrior("Thor", 22, 2, stamina = 12)

mage.attack(ranger)
ranger.attack(warrior)
warrior.attack(mage)
mage.attack(warrior)
warrior.attack(ranger)
ranger.attack(mage)
