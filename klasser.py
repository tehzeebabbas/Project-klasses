class karaktär:
    def __init__(self, namn, hälsa, attackkraft):
        self.namn = namn
        self.hälsa = hälsa
        self.attackkraft = attackkraft

class Mage(karaktär):
    def __init__(self, namn, hälsa, attackkraft, magi):
        super().__init__(self, namn, hälsa, attackkraft, magi)
        self.magi = magi
