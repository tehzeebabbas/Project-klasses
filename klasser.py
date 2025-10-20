class karaktär:
    def __init__(self, namn, hälsa, attackkraft):
        self.namn = namn
        self.hälsa = hälsa
        self.attackkraft = attackkraft

class Mage(karaktär):
    def __init__(self, namn, hälsa, attackkraft, mana):
        super().__init__(self, namn, hälsa, attackkraft, mana)
        self.mana = mana
