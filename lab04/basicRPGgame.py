class Item:
    def __init__(self, name = '', description = '', rarity = 'common'):
        self.itemname = name
        self.itemdescription = description
        self.itemrarity = rarity
        self._itemownership = ''
    
    def pick_up(self, character: str):
        self._itemownership = character
        return f"{self.itemname} is now owned by {self._itemownership}."
    
    def throw_away(self):
        self._itemownership = None
        return f"{self.itemname} is thrown away."
    
    def use(self):
        if self._itemownership is None:
            return ''
        else:
            return f"{self.itemname} is used."

        
class Weapon(Item):
    def __init__(self, name, description, rarity, damage = 0, type =''):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.weapontype = type
        self.active = False
        self.passive_attack_modifier = self.get_passive_modifier()

    def get_passive_modifier(self):
        if self.itemrarity == 'legendary':
            return 1.15 
        else:
            return 1.0

    def equip(self):
        if self._itemownership != False:
            self.active = True
            return f"{self.itemname} is equipped by {self._itemownership}."
    
    def use(self):
        if not self.active:
            return ''
        elif self._itemownership == False:
            return ''
        elif self.active == True:
            attackpower = self.damage * self.passive_attack_modifier
            return f"{self.itemname} is used, dealing {attackpower} damage."


class Shield(Item):
    def __init__(self, name, description, rarity = 'common', defense = 0, broken = False):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.active = False
        self.broken = broken
        self.passive_defense_modifier = self.get_passive_modifier()

    def get_passive_modifier(self):
        if self.itemrarity == 'legendary':
            return 1.10
        elif self.broken == True:
            return 0.5
        else:
            return 1.00

    def equip(self):
        if self._itemownership:
            self.active = True
            return f"{self.itemname} is equipped by {self._itemownership}."

    def use(self):
        if not self.active:
            return ''
        elif self._itemownership is None:
            return ''
        elif self.active == True:
            defensepower = self.defense * self.passive_defense_modifier
            return f"{self.itemname} is used, blocking {defensepower} damage."

class Potion(Item):
    def __init__(self, name, description ='', type ='', owner ='', value = 0, effective_time = 0):
        super().__init__(name, description, 'common')
        self.potion_type = type
        self.owner = owner
        self.value = value
        self.effective_time = effective_time
        self.used = False

    def from_ability(name, owner, type):
        if type == 'attack':
            value = 50
            effective_time = 30
        elif type == 'defense':
            value = 50
            effective_time = 30
        elif type == 'hp':
            value = 50
            effective_time = 0
        else:
            raise ValueError("Invalid type. Must be 'attack', 'defense', or 'hp'.")
        
        return Potion(name = name, type = type, owner = owner, value = value, effective_time = effective_time)

    def use(self):
        if self.used == False:
            self.used = True
            return f"{self.owner} used {self.itemname}, and attack increases {self.value} for {self.effective_time}s."
        else:
            return ''




belthronding = Weapon(name='Belthronding', description = 'a weapon to attack', rarity='legendary', damage=5000, type='bow')
print(belthronding.pick_up('Beleg'))  # Belthronding is now owned by Beleg
print(belthronding.equip())  # Belthronding is equipped by Beleg
print(belthronding.use())  # Belthronding is used, dealing 5750 damage



broken_pot_lid = Shield(name='wooden lid', description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield', defense = 5, broken = True)
print(broken_pot_lid.pick_up('Beleg'))  # wooden lid is now owned by Beleg
print(broken_pot_lid.equip())  # wooden lid is equipped by Beleg
print(broken_pot_lid.use())  # wooden lid is used, blocking 2.5 damage
print(broken_pot_lid.throw_away())  # wooden lid is thrown away
print(broken_pot_lid.use())  # NO OUTPUT


attack_potion = Potion.from_ability(name='atk potion temp', owner='Beleg', type ='attack')
print(attack_potion.use())  # Beleg used atk potion temp, and attack increases 50 for 30s
print(attack_potion.use())  # NO OUTPUT


print(isinstance(belthronding, Item))  # True
print(isinstance(broken_pot_lid, Shield))  # True
print(isinstance(attack_potion, Weapon))  # False