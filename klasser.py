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

class Ranger(karaktär):
    def __init__(self, namn, hälsa, attackkraft, energy):
        super().__init__(namn, hälsa, attackkraft)
        self.energy = energy

    def attack(self, other):
        damage = self.attackkraft + 1
        print(f"{self.namn} skjuter pil mot {other.namn} för {damage} skada")
        other.take_damage(damage)

class Warrior(karaktär):
    def __init__(self, namn, hälsa, attackkraft, stamina):
        super().__init__(namn, hälsa, attackkraft)
        self.stamina = stamina
   
    def attack(self, other):
        damage = self.attackkraft + 3
        print(f"{self.namn} svingar svärd mot {other.namn} för {damage} skada")
        other.take_damage(damage)

mage = Mage("Merlin", 20, 3, mana = 10)
ranger = Ranger("Robin", 18, 4, energy = 8)
warrior = Warrior("Thor", 22, 2, stamina = 12)

mage.attack(ranger)
ranger.attack(warrior)
warrior.attack(mage)
mage.attack(warrior)
warrior.attack(ranger)
ranger.attack(mage)
